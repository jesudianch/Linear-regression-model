
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the model and feature columns
model = joblib.load('linear_regression_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define request body
class PredictionRequest(BaseModel):
    data: dict

@app.post('/predict/')
async def predict(request: PredictionRequest):
    try:
        # Prepare input data
        input_data = pd.DataFrame([request.data])
        input_data_encoded = pd.get_dummies(input_data)
        
        # Align input data with training features
        input_data_encoded = input_data_encoded.reindex(columns=feature_columns, fill_value=0)
        
        # Make prediction
        prediction = model.predict(input_data_encoded)
        return {"prediction": prediction.tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
