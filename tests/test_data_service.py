import pytest
import os
import json
from services.data_service import DataService

# Test fixture to initialize DataService and create a temporary file
@pytest.fixture
def data_service(tmpdir):
    temp_file = tmpdir.join("test_predictions.ndjson")
    return DataService(data_file=str(temp_file))

def test_save_prediction(data_service):
    data = {
        "features": [8.3252, 41.0, 6.984127, 1.023809, 322.0, 2.555556, 37.88, -122.23],
        "predicted_price": [2.567]
    }
    result = data_service.save_prediction(data)
    assert result is True, "Failed to save prediction"

def test_retrieve_predictions(data_service):
    data = {
        "features": [8.3252, 41.0, 6.984127, 1.023809, 322.0, 2.555556, 37.88, -122.23],
        "predicted_price": [2.567]
    }
    data_service.save_prediction(data)
    predictions = data_service.retrieve_predictions()
    assert len(predictions) == 1, "Should retrieve exactly one prediction"
    assert predictions[0] == data, "Retrieved data does not match saved data"
