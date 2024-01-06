import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, f_classif

# Load the dataset
path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42)

# Standart scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Feature selection: Select the top 4 features
selector = SelectKBest(f_classif, k=4)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)


# Training the SVM classifier on the selected features
svm_selected = SVC(kernel='rbf')
svm_selected.fit(X_train_selected, y_train)

# Predicting the test set results
y_pred_selected = svm_selected.predict(X_test_selected)

# Calculating accuracy with selected features
accuracy_selected1 = accuracy_score(y_test, y_pred_selected)

print(accuracy_selected1)
