import pytest
from services.ml_service import MLService
import numpy as np

# Test fixtures are initialized before the tests, and are shared between them.
@pytest.fixture
def ml_service():
    return MLService()

def test_load_model(ml_service):
    assert ml_service.model is not None, "Model failed to load."

def test_predict_valid_input(ml_service):
    features = [8.3252, 41.0, 6.984127, 1.023809, 322.0, 2.555556, 37.88, -122.23]
    prediction = ml_service.predict(features)
    assert isinstance(prediction, np.ndarray), "Prediction should return a NumPy array."
    
def test_predict_invalid_input(ml_service):
    features = [8.3252, 41.0]
    prediction = ml_service.predict(features=features)
    assert prediction is None, "Prediction should fail with invalid inputs."