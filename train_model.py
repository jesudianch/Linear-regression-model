
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('Student_Performance.csv')

# Prepare data
X = data.drop(columns=['Performance Index'])
y = data['Performance Index']

# One-hot encode categorical columns
X_encoded = pd.get_dummies(X, drop_first=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and feature columns
joblib.dump(model, 'linear_regression_model.pkl')
joblib.dump(X_encoded.columns.tolist(), 'feature_columns.pkl')
