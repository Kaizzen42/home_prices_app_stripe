import joblib
import numpy as np
from constants import DEFAULT_MODEL_PATH


class MLService:
    def __init__(self, model_path=DEFAULT_MODEL_PATH):
        self.model_path = model_path
        self.model = self.load_model()
        
    def load_model(self):
        try:
            model = joblib.load(self.model_path)
            print(f"Model successfully loaded from path {self.model_path}")
            return model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
    
    def predict(self, features):
        try:
            features_array = np.array(features).reshape(1, -1)
            prediction = self.model.predict(features_array)
            return prediction[0]
        except Exception as e:
            print(f"Error making prediction on {features}. Caught Exception {e}")
            return None