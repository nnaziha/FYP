import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Generate synthetic therapy data
np.random.seed(2)
n = 150

data = pd.DataFrame({
    'age': np.random.randint(30, 70, size=n),
    'baseline_hba1c': np.random.normal(8, 1, size=n),
    'post_treatment_hba1c': np.random.normal(7, 1, size=n),
    'treatment_months': np.random.randint(1, 6, size=n)
})

# Label therapy as effective if HbA1c dropped by ≥0.5
data['effective'] = (data['baseline_hba1c'] - data['post_treatment_hba1c'] >= 0.5).astype(int)

print(data.head())

# Train/test split
X = data[['age', 'baseline_hba1c', 'post_treatment_hba1c', 'treatment_months']]
y = data['effective']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train classification model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probabilities
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluate using AUROC
auc = roc_auc_score(y_test, y_prob)
print(f'AUROC Score: {auc:.2f}')

