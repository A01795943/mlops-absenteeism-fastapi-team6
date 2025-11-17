import pandas as pd

def make_prediction(model, data: dict):
    df = pd.DataFrame([data])
    
    # Reordenar columnas según lo que espera el modelo
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(df)[0]
    return prediction
