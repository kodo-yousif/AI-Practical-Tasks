import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectFromModel


path = 'dataset.csv'

# Load the dataset
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

# Using Random Forest for feature importance
rf = RandomForestClassifier(n_estimators=100, random_state=2)
rf.fit(X_train, y_train)  

# Selecting features based on importance
selector = SelectFromModel(rf, prefit=True)
X_train_selected = selector.fit_transform(X_train)
X_test_selected = selector.transform(X_test)

# KNN Classifier with selected features
neighbors = range(1, 101, 2)
accuracies = []
max_accuracy3 = 0
optimal_i = 0

for i in neighbors:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train_selected, y_train)
    y_pred_knn = knn.predict(X_test_selected)
    accuracy= accuracy_score(y_pred_knn, y_test)
    accuracies.append(accuracy)
    if accuracy > max_accuracy3:
        max_accuracy3 = accuracy
        optimal_i = i
print(f"Maximum KNN accuracy is: {max_accuracy3}, Number of K is : {optimal_i}")

if __name__ == "__main__":
   plt.figure(figsize=(12, 6))
   plt.plot(neighbors, accuracies, marker='o')
   plt.xlabel('Number of Neighbors')
   plt.ylabel('Accuracy')
   plt.title('KNN Accuracy and Number of Neighbors')
   plt.xticks(range(min(neighbors), max(neighbors) + 1, 5))
   plt.grid(True)
   plt.show()