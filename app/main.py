from fastapi import FastAPI
from app.schemas import PredictionInput, PredictionOutput
from app.model_loader import load_model
from app.predictor import make_prediction
from typing import Any

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

# Cargar modelo
model = load_model()


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
    prediction = make_prediction(model, payload.data)
    return PredictionOutput(prediction=prediction)


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
