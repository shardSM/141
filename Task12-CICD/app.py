from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Train a small ML model when the app starts
iris = load_iris()
model = LogisticRegression(max_iter=200).fit(iris.data, iris.target)

app = Flask(__name__)
CORS(app)   # allows the frontend (Task 10) to call this API

@app.route("/")
def home():
    return "Iris AI model API is running"

@app.route("/predict", methods=["POST"])
def predict():
    features = request.get_json()["features"]   # 4 flower measurements
    pred = model.predict([features])[0]
    return jsonify({"species": str(iris.target_names[pred])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)   # 0.0.0.0 = reachable from outside the container
