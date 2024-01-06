import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the dataset
path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42)

# Training the SVM classifier on the selected features
svm_selected = SVC(kernel='rbf')
svm_selected.fit(X_train, y_train)

# Predicting the test set results
y_pred_selected = svm_selected.predict(X_train)
Traing_test=svm_selected.score(X_train,y_train)
Test_set_test=svm_selected.score(X_test,y_test)
# Calculating accuracy with selected features
accuracy_selected2 = accuracy_score(y_test, y_pred_selected)

print(accuracy_selected2)
print(f"Trainig test score is :{Traing_test}")
print(f"Testing test score is :{Test_set_test}")
