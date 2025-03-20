import pytest
from api.app import app


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

test_payload_2 = {
        "retailer": "AnotherStore",
        "purchaseDate": "2022-01-02",
        "purchaseTime": "15:30",
        "total": "10.25",
        "items": [
            {"shortDescription": "ItemOne", "price": "4.00"},
            {"shortDescription": "ItemTwo", "price": "6.25"}
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
    
def test_multiple_receipts(client):
    response1 = client.post('/receipts/process', json=test_payload)
    assert response1.status_code == 200
    receipt_id_1 = response1.get_json()["id"]
 
    get_response1 = client.get(f'/receipts/{receipt_id_1}/points')
    assert get_response1.status_code == 200
    points1 = get_response1.get_json()['points']
    expected_points1 = 20
    assert points1 == expected_points1

    response2 = client.post('/receipts/process', json=test_payload_2)
    assert response2.status_code == 200
    receipt_id_2 = response2.get_json()["id"]

    get_response2 = client.get(f'/receipts/{receipt_id_2}/points')
    assert get_response2.status_code == 200
    points2 = get_response2.get_json()['points']
    expected_points2 = 52
    assert points2 == expected_points2