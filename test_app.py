import pytest
from app import app
from uuid import UUID

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
test_payload = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "total": "6.49",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"}
        ]
    }

def test_wrong_request(client):
    fake_id = 12345
    response = client.get(f'/receipts/{fake_id}/process', json=test_payload)
    print(response.data)
    assert response.status_code == 404


def test_valid_receipt(client):
    response = client.post('/receipts/process', json=test_payload)
    assert response.status_code == 200
    
    data = response.get_json()
    assert "id" in data
        
    get_response = client.get(f'receipts/{data["id"]}/points')
    assert get_response.status_code == 200
    
    print(get_response.get_json())
    
    assert get_response.get_json()['points'] == 20
    
    
def test_no_payload(client):
    response = client.post('/receipts/process', json={})
    assert response.status_code == 400
    
