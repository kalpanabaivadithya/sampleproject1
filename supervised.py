# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Models
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier

# Metrics
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error, r2_score

# -------------------------------
# 1. CLASSIFICATION (IRIS DATASET)
# -------------------------------
print("\n=== Classification: Iris Dataset ===")

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model 1: Logistic Regression
model1 = LogisticRegression()
model1.fit(X_train, y_train)
y_pred1 = model1.predict(X_test)

print("\nLogistic Regression Accuracy:", accuracy_score(y_test, y_pred1))

# Model 2: Random Forest
model2 = RandomForestClassifier(n_estimators=100)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, y_pred2))

# Confusion Matrix
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred2))

# -------------------------------
# 2. REGRESSION (HOUSING DATASET)
# -------------------------------
print("\n=== Regression: California Housing Dataset ===")

# Load dataset
housing = fetch_california_housing()
Xh = housing.data
yh = housing.target

# Split data
Xh_train, Xh_test, yh_train, yh_test = train_test_split(Xh, yh, test_size=0.2, random_state=42)

# Model: Linear Regression
reg_model = LinearRegression()
reg_model.fit(Xh_train, yh_train)
yh_pred = reg_model.predict(Xh_test)

# Evaluation
mse = mean_squared_error(yh_test, yh_pred)
r2 = r2_score(yh_test, yh_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# -------------------------------
# 3. VISUALIZATION
# -------------------------------
plt.figure(figsize=(6,4))
plt.sc
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted (Regression)")
plt.show()