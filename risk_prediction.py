import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

# === 1. Load Dataset ===
data = pd.read_csv("DrLim1000Synthetic.csv")

# === 2. Encode Categorical Features ===
label_cols = ['Gender', 'Insulin_Regimen', 'CKD_Stage']
for col in label_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

# === 3. Select Features and Target ===
features = [
    'Age', 'Gender', 'Duration_DM', 'Insulin_Regimen', 'DDS_1st',
    'HbA1c', 'Freq_SMBG', 'Freq_Hypo', 'Freq_Visits', 'eGFR', 'CKD_Stage'
]
target = 'HbA1c'  # Changed from Predicted_HbA1C due to constant values

X = data[features]
y = data[target]

# === 4. Train-Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 5. Train Random Forest Regressor ===
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === 6. Evaluate Model ===
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"\n📉 Mean Absolute Error (MAE): {mae:.3f}")

# === 7. Feature Importance ===
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print("\n📈 Top Feature Importances:")
print(importances.head(10))
