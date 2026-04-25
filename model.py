import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("data.csv")

X = data[["temperature", "humidity", "soil_moisture"]]
y = data["water_needed"]

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_irrigation(temp, humidity, moisture):
    return int(model.predict([[temp, humidity, moisture]])[0])