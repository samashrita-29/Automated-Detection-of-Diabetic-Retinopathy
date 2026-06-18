from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Diabetic Retinopathy Detection System"

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    # Placeholder prediction
    result = {
        "prediction": "DR Detected",
        "confidence": 0.87
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
