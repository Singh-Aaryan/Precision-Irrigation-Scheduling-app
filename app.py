from flask import Flask, render_template, request
from model import predict_irrigation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        temp = request.form.get("temperature")
        humidity = request.form.get("humidity")
        moisture = request.form.get("moisture")

        if temp and humidity and moisture:
            prediction = predict_irrigation(float(temp), float(humidity), float(moisture))

            if prediction == 1:
                result = "💧 Irrigation Needed"
            else:
                result = "✅ No Irrigation Needed"
        else:
            result = "⚠️ Fill all fields"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from model import predict_irrigation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        print("FORM DATA:", request.form)   # 👈 DEBUG

        temp = request.form.get("temperature")
        humidity = request.form.get("humidity")
        moisture = request.form.get("moisture")

        print(temp, humidity, moisture)  # 👈 DEBUG

        if temp and humidity and moisture:
            prediction = predict_irrigation(float(temp), float(humidity), float(moisture))

            print("Prediction:", prediction)  # 👈 DEBUG

            if prediction == 1:
                result = "💧 Irrigation Needed"
            else:
                result = "✅ No Irrigation Needed"
        else:
            result = "⚠️ Fill all fields"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)