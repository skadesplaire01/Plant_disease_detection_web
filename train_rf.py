import os
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import json

# --- 1. Load dataset ---
dataset_path = 'dataset'
X, y = [], []
class_names = sorted(os.listdir(dataset_path))
class_indices = {name: idx for idx, name in enumerate(class_names)}

for class_name in class_names:
    folder = os.path.join(dataset_path, class_name)
    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        try:
            img = Image.open(img_path).convert('RGB').resize((64,64))
            X.append(np.array(img).flatten())  # flatten for Random Forest
            y.append(class_indices[class_name])
        except:
            pass  # skip corrupted images

X = np.array(X)
y = np.array(y)

# --- 2. Split dataset ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 3. Train Random Forest ---
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# --- 4. Evaluate ---
y_pred = clf.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))

# --- 5. Save model ---
joblib.dump(clf, 'rf_model.pkl')

# --- 6. Save class names ---
with open('class_names.json', 'w') as f:
    json.dump(class_names, f)

print("Model saved as rf_model.pkl")
