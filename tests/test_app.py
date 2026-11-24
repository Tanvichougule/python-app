from app import app

def test_homepage():
    app.config['TESTING'] = True

    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert b"Welcome to My Python Application!" in response.data

def test_button_content():
    app.config['TESTING'] = True

    client = app.test_client()

    response = client.get('/')

    assert b"Click Me" in response.data
