from flask import Blueprint, jsonify, request

# Define the blueprint
prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # features = np.array(data['features'].reshape(1, -1))
    # prediction = model.predict(features)
    prediction = [2400000]
    return jsonify({'predicted_price': prediction[0]})

@prediction_bp.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    return jsonify({'status': 'Data saved successfully'})

@prediction_bp.route('/retrieve', methods=['GET'])
def retrieve_data():
    return jsonify({'data': 'Sample Data'})
