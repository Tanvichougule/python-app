
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'index.html',
        prediction=None,
        stock=None,
        message=None,
        error=None
    )


@app.route('/predict', methods=['POST'])
def predict():
    stock = request.form.get('stock', '').strip().upper()

    if not stock:
        return render_template(
            'index.html',
            prediction=None,
            stock=None,
            message=None,
            error="Please enter a stock symbol."
        )

    allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"

    if not all(character in allowed_characters for character in stock):
        return render_template(
            'index.html',
            prediction=None,
            stock=None,
            message=None,
            error="Please enter a valid stock symbol."
        )

    # Demo calculation only; this is not a real stock prediction.
    demo_value = sum(ord(character) for character in stock) * 1.25

    prediction = f"${demo_value:.2f}"
    message = "This is a demo estimate, not real market data."

    return render_template(
        'index.html',
        prediction=prediction,
        stock=stock,
        message=message,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True)
