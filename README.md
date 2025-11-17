# 📘 Absenteeism Prediction API

Este proyecto expone un modelo de Machine Learning para predecir el ausentismo laboral mediante un endpoint REST construido con **FastAPI**.  
Incluye documentación automática con **Swagger/OpenAPI**, versionamiento del modelo y un pipeline simple de inferencia.

---

## 📦 Artefacto del Modelo

El modelo utilizado proviene del registro interno con la siguiente ruta:

```
models:/absenteeism_model/1.0.0
```

En este repositorio se incluye la versión serializada:

```
model.joblib
```

---

## 🚀 Instrucciones para Ejecutar la API

### 1. Crear entorno virtual

```
python3 -m venv venv
```

En macOS/Linux:

```
source venv/bin/activate
```

En Windows:

```
venv\Scripts\activate
```

### 2. Instalar dependencias

```
pip install -r requirements.txt
```

### 3. Iniciar el servidor

```
uvicorn main:app --reload
```

La API estará disponible en:

```
http://localhost:8000
```

---

## 📝 Documentación Swagger / OpenAPI

FastAPI genera la documentación automáticamente:

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## 🔌 Endpoints

### POST /predict

Genera una predicción basada en los datos enviados.

Ejemplo de entrada:

```
{
  "data": {
    "Reason for absence_0": 0,
    "Reason for absence_1": 1,
    "Month of absence_1": 0,
    "Day of the week_2": 1,
    "Seasons_1": 0,
    "Disciplinary failure_False": 1,
    "Transportation expense": 200,
    "Distance from Residence to Work": 10,
    "Service time": 5,
    "Age": 30,
    "Work load Average/day": 250,
    "Hit target": 95,
    "Son": 1,
    "Pet": 0,
    "Weight": 70,
    "Height": 170,
    "Body mass index": 24,
    "Absenteeism time in hours": 0,
    "Dependents_count": 1,
    "Has_dependents": 1,
    "Lifestyle_risk_score": 5,
    "Healthy_lifestyle": 1,
    "Penalty_risk_score": 2,
    "Reliability_score": 8,
    "Reliability_score_norm": 0.65,
    "Workload_deviation": 3
  }
}
```

Ejemplo de salida:

```
{
  "prediction": 2
}
```

---

### GET /features

Devuelve todas las columnas/variables usadas por el modelo.

Ejemplo de salida:

```
{
  "features": [
    "Reason for absence_0",
    "Reason for absence_1",
    "Reason for absence_3",
    "Reason for absence_4",
    "Reason for absence_5",
    "Reason for absence_6",
    "Reason for absence_7",
    "Reason for absence_8",
    "Reason for absence_9",
    "Reason for absence_10",
    "Reason for absence_11",
    "Reason for absence_12",
    "Reason for absence_13",
    "Reason for absence_14",
    "Reason for absence_15",
    "Reason for absence_16",
    "Reason for absence_17",
    "Reason for absence_18",
    "Reason for absence_19",
    "Reason for absence_21",
    "Reason for absence_22",
    "Reason for absence_23",
    "Reason for absence_24",
    "Reason for absence_25",
    "Reason for absence_26",
    "Reason for absence_27",
    "Reason for absence_28",
    "Month of absence_1",
    "Month of absence_10",
    "Month of absence_11",
    "Month of absence_12",
    "Month of absence_2",
    "Month of absence_3",
    "Month of absence_4",
    "Month of absence_5",
    "Month of absence_6",
    "Month of absence_7",
    "Month of absence_8",
    "Month of absence_9",
    "Day of the week_2",
    "Day of the week_3",
    "Day of the week_4",
    "Day of the week_5",
    "Day of the week_6",
    "Seasons_1",
    "Seasons_2",
    "Seasons_3",
    "Seasons_4",
    "Disciplinary failure_False",
    "Disciplinary failure_True",
    "Education_1",
    "Education_2",
    "Education_3",
    "Social drinker_False",
    "Social drinker_True",
    "Social smoker_False",
    "Social smoker_True",
    "Transportation expense",
    "Distance from Residence to Work",
    "Service time",
    "Age",
    "Work load Average/day",
    "Hit target",
    "Son",
    "Pet",
    "Weight",
    "Height",
    "Body mass index",
    "Absenteeism time in hours",
    "Dependents_count",
    "Has_dependents",
    "Lifestyle_risk_score",
    "Healthy_lifestyle",
    "Penalty_risk_score",
    "Reliability_score",
    "Reliability_score_norm",
    "Workload_deviation"
  ]
}
```

---

## 📂 Estructura del Proyecto

```
.
├── app/
│   ├── schemas.py
│   ├── predictor.py
│   ├── model_loader.py
│   └── ...
├── main.py
├── model.joblib
├── requirements.txt
└── README.md
```

---

## 🧠 Lógica del Pipeline de Predicción

- El endpoint toma el JSON recibido.
- Extrae `payload.data`.
- Alinea los valores en el orden exacto del modelo.
- Ejecuta:
  - model.predict()
- Devuelve el resultado en JSON.

---

## Docker

### 1. Construir la imagen

docker build -t mlops-team6/ml-service:latest .

### 2. Ejecutar el contenedor

docker run -p 8000:8000 mlops-team6/ml-service:latest

La API estará disponible en:

http://localhost:8000

---

## Dockerfile
```
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
 build-essential \
 && rm -rf /var/lib/apt/lists/\*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
 pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
## 🏷 Versión de la API

```
1.0.0
```
