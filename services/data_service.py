import json
import os
from constants import PREDICTIONS_DATA_PATH
import datetime

class DataService:
    def __init__(self, data_file=PREDICTIONS_DATA_PATH):
        self.data_file = data_file
        
    def save_prediction(self, data):
        try:
            if not os.path.exists(os.path.dirname(self.data_file)):
                os.makedirs(os.path.dirname(self.data_file))
           
            with open(self.data_file, 'a') as f:
                json.dump(data, f)
                f.write("\n")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        
    def retrieve_predictions(self):
        try:
            with open(self.data_file, 'r') as f:
                return [json.loads(line) for line in f]
        except Exception as e:
            print(f"Error retrieving data from {self.data_file}: {e}")
            return []