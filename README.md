# Python App

A simple web application developed using Python, Flask, HTML and CSS.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Gunicorn
- Pytest

## Project Structure

python-app/
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── tests/
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── README.md
└── Jenkinsfile

## Installation

1. Clone the repository:

   git clone https://github.com/YOUR-USERNAME/python-app.git

2. Navigate to the project:

   cd python-app

3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   python3 app.py

5. Open your browser:

   http://127.0.0.1:5000

## Testing

Run the tests using:

pytest

## Deployment

This application can be deployed on an AWS EC2 instance
using Gunicorn and Nginx.
