# tests/test_app.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data
