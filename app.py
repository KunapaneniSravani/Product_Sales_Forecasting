from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load Model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Product Sales Forecast API is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"Predicted_Sales": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
