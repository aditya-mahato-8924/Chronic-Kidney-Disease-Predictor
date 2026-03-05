from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import Model

# create a FastAPI app
app = FastAPI(title='Chronic Kidney Disease Predictor API',
              description='API for predicting chronic kidney disease based on patient data',
              version='1.0.0')

# create an instance of the model
model = Model()

# fetch the metadata of the model
model_metadata = model.get_model_metadata()

# define a route for the root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Chronic Kidney Disease Predictor API!"}

# define health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK",
            "model_loaded": model_metadata["model_loaded"],
            "model_version": model_metadata["model_version"]}

# define a route for the prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserInput):
    try:
        # make prediction using the model
        prediction_result = model.predict(data)
        return JSONResponse(status_code=200, content=prediction_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
