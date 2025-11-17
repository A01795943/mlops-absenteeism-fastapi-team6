📘 Absenteeism Prediction API

Este proyecto expone un modelo de Machine Learning para predecir el ausentismo laboral mediante un endpoint REST construido con FastAPI.
Incluye documentación automática con Swagger/OpenAPI, versionamiento del modelo y un pipeline simple de inferencia.

📦 Artefacto del Modelo

El modelo utilizado proviene del registro interno con la siguiente ruta:

models:/absenteeism_model/1.0.0

En este repositorio se incluye la versión serializada:

model.joblib

🚀 Instrucciones para Ejecutar la API

1. Crear entorno virtual
   python3 -m vvenv venv

En macOS/Linux:

source venv/bin/activate

En Windows:

venv\Scripts\activate

2. Instalar dependencias
   pip install -r requirements.txt

3. Iniciar el servidor
   uvicorn main:app --reload

La API estará disponible en:

http://localhost:8000

📝 Documentación Swagger / OpenAPI

FastAPI genera la documentación automáticamente:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

🔌 Endpoints
POST /predict

Genera una predicción basada en los datos enviados.

Ejemplo de entrada:

{
"data": {
"age": 35,
"years_of_employment": 5.2,
"previous_year_absences": 3,
"distance_from_home": 12.5
}
}

Ejemplo de salida:

{
"prediction": 1,
"probability": 0.78
}

GET /features

Devuelve todas las columnas/variables usadas por el modelo.

Ejemplo de salida:

{
"features": [
"Reason for absence_0",
"Reason for absence_1",
"Reason for absence_3",
"...",
"Workload_deviation"
]
}

📂 Estructura del Proyecto
.
├── app/
│ ├── schemas.py
│ ├── predictor.py
│ ├── model_loader.py
│ └── ...
├── main.py
├── model.joblib
├── requirements.txt
└── README.md

🧠 Lógica del Pipeline de Predicción

El endpoint toma el objeto JSON recibido.

Se transforma en un vector con el mismo orden de columnas que el modelo espera.

Se ejecuta:

model.predict()

model.predict_proba()

Se devuelve el resultado en formato JSON.

🛠 Requisitos Técnicos

Python 3.10+

FastAPI

Uvicorn

Joblib

scikit-learn

🏷 Versión de la API
1.0.0
