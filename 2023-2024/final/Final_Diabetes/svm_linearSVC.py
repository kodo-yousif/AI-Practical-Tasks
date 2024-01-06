import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel

# Load the dataset
path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Feature Selection with LinearSVC
lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X_train_scaled, y_train)
model = SelectFromModel(lsvc, prefit=True)
X_train_selected = model.transform(X_train_scaled)
X_test_selected = model.transform(X_test_scaled)

# Training the SVM classifier on the selected features
svm_selected = SVC(kernel='linear')
svm_selected.fit(X_train_selected, y_train)

# Predicting the test set results
y_pred_selected = svm_selected.predict(X_test_selected)

# Calculating accuracy with selected features
accuracy_selected2 = accuracy_score(y_test, y_pred_selected)

# Identify the selected features
selected_features = X.columns[model.get_support()]

print(accuracy_selected2)
print(selected_features.tolist())
