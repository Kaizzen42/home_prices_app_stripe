from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize the Flask Application
app = Flask(__name__)

# Load the config
app.config.from_object('config.Config')

# Import and register blueprints
from routes.prediction_routes import prediction_bp
app.register_blueprint(prediction_bp)

@app.route('/')
def home():
    return "Welcome to the House Price Prediction API!"

if __name__ == '__main__':
    app.run(debug=True)