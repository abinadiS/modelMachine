import joblib
import numpy as np
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/predict", methods=["GET"])
def predict():
    X_test = np.array(
        [
            6.73925056,
            6.564749341,
            1.25278461,
            1.284024954,
            0.819479704,
            0.376895279,
            0.326662421,
            0.082287982,
            2.509585857,
        ]
    )
    prediction = model.predict(X_test.reshape(1, -1))
    return jsonify({"prediction": list(prediction)})


if __name__ == "__main__":
    model = joblib.load("./models/best_model.pkl")
    app.run(port=8080)
