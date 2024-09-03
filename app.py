import numpy as np
from flask import Flask, render_template, request
from services import ml_service
from services.ml_service import MLService

# Initialize the Flask Application
app = Flask(__name__)
ml_service = MLService()

# Load the config
app.config.from_object('config.Config')

# Import and register blueprints
from routes.prediction_routes import prediction_bp
app.register_blueprint(prediction_bp)

@app.route('/', methods=['GET','POST'])
def index():
    prediction = None
    feature_averages = ml_service.feature_averages
    feature_averages = [np.round(f, 2) for f in feature_averages]
     # Initialize feature_values with averages as defaults
    feature_values = {
        'MedInc': feature_averages[0],
        'HouseAge': feature_averages[1],
        'AveRooms': feature_averages[2],
        'AveBedrms': feature_averages[3],
        'Population': feature_averages[4],
        'AveOccup': feature_averages[5],
        'Latitude': feature_averages[6],
        'Longitude': feature_averages[7]
    }

    if request.method == 'POST':
        # Overwrite feature_values with the user input
        feature_values = {
            'MedInc': float(request.form.get('MedInc', feature_averages[0])),
            'HouseAge': float(request.form.get('HouseAge', feature_averages[1])),
            'AveRooms': float(request.form.get('AveRooms', feature_averages[2])),
            'AveBedrms': float(request.form.get('AveBedrms', feature_averages[3])),
            'Population': float(request.form.get('Population', feature_averages[4])),
            'AveOccup': float(request.form.get('AveOccup', feature_averages[5])),
            'Latitude': float(request.form.get('Latitude', feature_averages[6])),
            'Longitude': float(request.form.get('Longitude', feature_averages[7]))
        }
        
        # Use the feature_values for prediction
        features = [
            feature_values['MedInc'],
            feature_values['HouseAge'],
            feature_values['AveRooms'],
            feature_values['AveBedrms'],
            feature_values['Population'],
            feature_values['AveOccup'],
            feature_values['Latitude'],
            feature_values['Longitude']
        ]
        
        prediction = ml_service.predict(features)
        prediction = prediction[0] if isinstance(prediction, (list, tuple, np.ndarray)) else prediction
    
    # Always pass feature_values and feature_averages to the template
    return render_template('index.html', prediction=prediction, feature_averages=feature_averages, feature_values=feature_values)


if __name__ == '__main__':
    app.run(debug=True)