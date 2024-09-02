import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_route(client):
    response = client.post('/predict', json={
        "features": [8.3252, 41.0, 6.984127, 1.023809, 322.0, 2.555556, 37.88, -122.23]
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert "predicted_price" in json_data

def test_retrieve_route(client):
    # Assuming there's already data to retrieve
    response = client.get('/retrieve')
    json_data = response.get_json()
    assert response.status_code == 200
    assert isinstance(json_data, list)
