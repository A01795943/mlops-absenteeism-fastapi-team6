from fastapi import FastAPI
from app.schemas import PredictionInput, PredictionOutput
from app.model_loader import load_model
from app.predictor import make_prediction
from typing import Any
import pandas as pd
import json
import os
import logging

# ==============================
# Logging dual: archivo + consola
# ==============================
LOG_PATH = "monitoring/drift.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
fh = logging.FileHandler(LOG_PATH)
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(fh)
logger.addHandler(ch)

# ==============================
# FastAPI app
# ==============================
app = FastAPI(
    title="Absenteeism ML Model Serving API",
    version="1.0.0",
    description="""
API para exponer un modelo de Machine Learning que predice horas de ausentismo laboral.

**Modelo:** models:/absenteeism_model/1.0.0  
**Entradas:** 82 features preprocesados  
**Salida:** Predicción numérica de horas de ausencia  
""",
)

# ==============================
# Cargar modelo
# ==============================
model = load_model()

# ==============================
# Cargar baseline de drift
# ==============================
BASELINE_PATH = "monitoring/baseline_profile.json"
if os.path.exists(BASELINE_PATH):
    with open(BASELINE_PATH) as f:
        baseline = json.load(f)
else:
    baseline = None
    logging.warning("⚠️ Baseline de drift no encontrado. /predict no reportará drift.")

# ==============================
# Endpoints
# ==============================
@app.post(
    "/predict",
    response_model=PredictionOutput,
    tags=["Predicción"],
    summary="Realiza una predicción con el modelo",
    description="""
Envía un diccionario con todas las features utilizadas por el modelo dentro del campo `data`.

Ejemplo disponible en el esquema de Swagger.
""",
)
def predict(payload: PredictionInput):
    # Convertir input a DataFrame
    df_input = pd.DataFrame([payload.data])

    # Hacer predicción
    prediction = make_prediction(model, payload.data)

    drift_report = {}
    alert_triggered = False

    if baseline:
        for col in baseline.keys():
            if col in df_input.columns:
                # Drift si se sale de 3 sigmas del baseline
                mean = baseline[col]["mean"]
                std = baseline[col]["std"]
                value = df_input[col].iloc[0]

                drift_detected = abs(value - mean) > 3 * std
                drift_report[col] = {
                    "drift_detected": drift_detected,
                    "value": float(value),
                    "baseline_mean": mean,
                    "baseline_std": std
                }

                if drift_detected:
                    alert_triggered = True

        # Loguear alerta si hay drift
        if alert_triggered:
            logging.warning(f"ALERTA DRIFT: Valores con drift detectado: {drift_report}")

    return PredictionOutput(prediction=prediction, drift_report=drift_report)


@app.get(
    "/features",
    tags=["Información del modelo"],
    summary="Obtén la lista de features utilizadas por el modelo",
    description="""
Retorna el listado completo de columnas (`feature_names_in_`) que el modelo espera como entrada.
""",
)
def get_model_features():
    return {"features": list(model.feature_names_in_)}
