from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib
import os
from constants import MODEL_DIR, HOUSE_PRICE_MODE_NAME

# Load the dataset
california = fetch_california_housing()
X = california.data
y = california.target

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

test_preds = model.predict(X_test)
mae_test = mean_absolute_error(y_true=y_test, y_pred=test_preds)
print(f"Test MAE = {mae_test}")

# Define the model dir, and save the model
model_dir = MODEL_DIR
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, HOUSE_PRICE_MODE_NAME)
joblib.dump(model, model_path)

print(f"Model trained, and saved to {model_path}")