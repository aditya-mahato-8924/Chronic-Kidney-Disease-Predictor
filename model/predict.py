import pickle
from schema.user_input import UserInput
import pandas as pd

MODEL_PATH = r"model/rf_grid_search.pkl"

class Model:
    def __init__(self):
        with open(MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)
        
        self.__model_loaded = True if self.model else False
        self.__MODEL_VER = "1.0.0" if self.__model_loaded else None

    # getter for model metadata
    def get_model_metadata(self):
        return {
            "model_version": self.__MODEL_VER,
            "model_loaded": self.__model_loaded
        }
    
    # utility function to convert user input to dataframe
    def __convert_input_to_dataframe(self, user_input: UserInput):
        input_dict = user_input.model_dump()
        df = pd.DataFrame([input_dict])
        return df
    
    # utility function to get class labels from prediction
    def __get_class_labels(self, prediction):
        # define class labels
        class_labels = {
            0: "Not Chronic Kidney Disease",
            1: "Chronic Kidney Disease"
        }
        
        # return class label
        return class_labels.get(prediction, "Unknown")
    
    
    # utility function to return feature importance
    def __return_feature_importance(self, input_df:pd.DataFrame, predicted_category:int):
        if not self.__model_loaded:
            raise Exception("Model not loaded")
        
        # get feature importance
        feature_imp = self.model.best_estimator_.named_steps['model'].feature_importances_.round(2)

        # return feature importance
        return dict(zip(input_df.columns, feature_imp))
    

    # main prediction function
    def predict(self, user_input: UserInput):
        if not self.__model_loaded:
            raise Exception("Model not loaded")
        
        # convert user input to dataFrame
        input_df = self.__convert_input_to_dataframe(user_input)

        # make prediction
        prediction = self.model.predict(input_df)
        predicted_category = self.__get_class_labels(int(prediction[0]))
        probability = self.model.predict_proba(input_df)[0][prediction[0]]


        # return prediction
        return {
            "predicted_category": predicted_category,
            "predicted_probability": round(float(probability), 2),
            "feature_importance": self.__return_feature_importance(input_df, int(prediction[0])),
            "disclaimer": "This prediction is for informational purposes only and should not be considered as medical advice. Always consult with a healthcare professional for medical concerns."
        }