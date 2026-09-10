import requests

BASE_URL = "https://katalon-demo-cura.herokuapp.com"

def test_api_valid_login_backend():
   
    url = f"{BASE_URL}/authenticate.php"
    payload = {
        "username": "John Doe",
        "password": "ThisIsNotAPassword"
    }
    
   
    response = requests.post(url, data=payload)
    
   
    assert response.status_code == 200
    
   
    assert response.elapsed.total_seconds() < 2.0, "API seems slow"

def test_api_invalid_login_backend():
   
    url = f"{BASE_URL}/authenticate.php"
    payload = {
        "username": "John Doe",
        "password": "WrongPassword"
    }
    
    response = requests.post(url, data=payload)
    
    assert response.status_code == 200
    assert "Login failed" in response.text