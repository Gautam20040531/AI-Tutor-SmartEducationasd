import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

# Load dataset
df = pd.read_csv("data/ai_training.csv")

# Split features & labels
X = df[['study_hours', 'attendance', 'previous_score']]
y = df['final_score']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN Model
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)

# Save Model
joblib.dump(knn, "models/knn_model.pkl")

print("KNN Model Trained & Saved!")
