from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open(r"C:\Users\Prash\Desktop\Workspace\Car Price Prediction\models\car_price_prediction.pkl", "rb"))

@app.route("/")
def home():
    # IMPORTANT FIX: do not show prediction at start
    return render_template("car_price_prediction.html", prediction_text=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect all 21 features IN EXACT ORDER the model expects
        features = [
            float(request.form["region"]),          # 1
            float(request.form["year"]),            # 2
            float(request.form["manufacturer"]),    # 3
            float(request.form["model"]),           # 4
            float(request.form["condition"]),       # 5
            float(request.form["cylinders"]),       # 6
            float(request.form["fuel"]),            # 7
            float(request.form["odometer"]),        # 8
            float(request.form["title_status"]),    # 9
            float(request.form["transmission"]),    # 10
            float(request.form["drive"]),           # 11
            float(request.form["size"]),            # 12
            float(request.form["type"]),            # 13
            float(request.form["paint_color"]),     # 14
            float(request.form["state"]),           # 15
            float(request.form["lat"]),             # 16
            float(request.form["long"]),            # 17
            float(request.form["posting_date"]),    # 18
            float(request.form["posting_day"]),     # 19
            float(request.form["posting_month"]),   # 20
            float(request.form["posting_year"])     # 21
        ]

        final = np.array(features).reshape(1, -1)
        prediction = model.predict(final)[0]
        prediction = round(prediction, 2)

        return render_template("car_price_prediction.html",
                               prediction_text=f"Predicted Price: ${prediction}")

    except Exception as e:
        return f"Error during prediction: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
