
from app import app


def test_homepage():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert b"StockPredict" in response.data
    assert b"Predict a" in response.data


def test_prediction():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.post('/predict', data={'stock': 'AAPL'})

    assert response.status_code == 200
    assert b"AAPL" in response.data
    assert b"Prediction Result" in response.data
    assert b"$" in response.data


def test_empty_stock():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.post('/predict', data={'stock': ''})

    assert response.status_code == 200
    assert b"Please enter a stock symbol." in response.data


def test_invalid_stock():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.post('/predict', data={'stock': 'AAPL@123'})

    assert response.status_code == 200
    assert b"Please enter a valid stock symbol." in response.data
