from flask import Blueprint, jsonify, request
from services.ml_service import MLService

# Define the blueprint
prediction_bp = Blueprint('prediction', __name__)

# Initialize the ML Service
ml_service = MLService()

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features', [])
    if not features:
        return jsonify({'error': 'No features provided'}), 400
    
    predicted_price = ml_service.predict(features)
    
    if not predicted_price:
        return jsonify({'error': 'Prediction Failed'}), 500
        
    return jsonify({'predicted_price': predicted_price[0]})

@prediction_bp.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    return jsonify({'status': 'Data saved successfully'})

@prediction_bp.route('/retrieve', methods=['GET'])
def retrieve_data():
    return jsonify({'data': 'Sample Data'})
