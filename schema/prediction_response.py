from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    prediction: str = Field(..., description="Predicted category for chronic kidney disease")
    probability: float = Field(..., description="Predicted probability for the predicted category")
    feature_importance: Dict[str, float] = Field(..., description="Feature importance values for the input features")
    disclaimer: str = Field(..., description="Disclaimer for the prediction results")