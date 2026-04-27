# Import libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset (example: built-in dataset)
from sklearn.datasets import load_iris

# Load data
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Apply StandardScaler
scaler = StandardScaler()

# Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

# Convert back to DataFrame (optional for display)
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)

# Display results
print("Original Training Data (first 5 rows):")
print(X_train.head())

print("\nScaled Training Data (first 5 rows):")
print(X_train_scaled.head())

print("\nMean after scaling (should be ~0):")
print(X_train_scaled.mean())

print("\nStandard deviation after scaling (should be ~1):")
print(X_train_scaled.std())