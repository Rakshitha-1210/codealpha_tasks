import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

os.makedirs("visuals", exist_ok=True)

# Load dataset
df = pd.read_csv("data/advertising.csv")

print(df.head())

# Features
X = df.drop("Sales", axis=1)

# Target
y = df["Sales"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Model
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Metrics
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Visualization
plt.figure(figsize=(10,5))

plt.plot(y_test.values[:20], label="Actual Sales")
plt.plot(predictions[:20], label="Predicted Sales")

plt.xlabel("Samples")
plt.ylabel("Sales")
plt.title("Actual vs Predicted Sales")

plt.legend()

plt.savefig("visuals/sales_prediction.png")
plt.show()