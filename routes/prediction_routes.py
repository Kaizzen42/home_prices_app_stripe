import datetime
from flask import Blueprint, jsonify, request
from services.ml_service import MLService
from services.data_service import DataService
import numpy as np

# Define the blueprint
prediction_bp = Blueprint('prediction', __name__)

# Initialize the ML Service
ml_service = MLService()
# Initialize data service
data_service = DataService()

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features', [])
    if not features:
        return jsonify({'error': 'No features provided'}), 400
    
    predicted_price = ml_service.predict(features)
    if not predicted_price:
        return jsonify({'error': 'Prediction Failed'}), 500

    # Needed for JSON serialization
    if isinstance(predicted_price, np.ndarray):
        predicted_price = predicted_price.tolist()
    timestamp = datetime.datetime.now().isoformat() 
    prediction_data = {
        'features': features, 
        'predicted_price': predicted_price,
        'timestamp': timestamp
    }        
    
    # Save the prediction to the datastore
    data_service.save_prediction(prediction_data)
    
    return jsonify({'predicted_price': predicted_price})

@prediction_bp.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    return jsonify({'status': 'Data saved successfully'})

@prediction_bp.route('/retrieve', methods=['GET'])
def retrieve_data():
    predictions = data_service.retrieve_predictions()
    return jsonify(predictions)
