import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt



path='dataset.csv'

load_dataset=pd.read_csv(path)
X, y = load_dataset.drop('Outcome',axis=1),load_dataset['Outcome']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.3, random_state=2)


neighbors = range(1, 103, 2)
accuracies = []
max_accuracy4 = 0
optimal_i = 0

for i in neighbors:
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train)
    y_predict = neigh.predict(X_test)
    accuracy = accuracy_score(y_predict, y_test)
    accuracies.append(accuracy)
    max_value=max(accuracies)
    if accuracy > max_accuracy4:
        max_accuracy4 = accuracy
        optimal_i = i
print(f"maximum accuarcy is: {max_value}, Number of K is: {optimal_i}")

if __name__ == "__main__":
   plt.figure(figsize=(12, 6))
   plt.plot(neighbors, accuracies, marker='o')
   plt.xlabel('Number of Neighbors')
   plt.ylabel('Accuracy')
   plt.title('KNN Accuracy and Number of Neighbors')
   plt.xticks(range(min(neighbors), max(neighbors) + 1, 5))
   plt.grid(True)
   plt.show()

