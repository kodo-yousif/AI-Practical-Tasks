import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest,mutual_info_classif


path='dataset.csv'

load_dataset=pd.read_csv(path)
X, y = load_dataset.drop('Outcome',axis=1),load_dataset['Outcome']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.3, random_state=2)

# Feature selection: Select the top 4 features
selector = SelectKBest(mutual_info_classif, k=4)
X_train_selected = selector.fit_transform(X_train, y_train)  
X_test_selected = selector.transform(X_test)


neighbors = range(1, 101, 2)
accuracies = []
max_accuracy2 = 0
optimal_i = 0

for i in neighbors:
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train_selected, y_train)
    y_predict = neigh.predict(X_test_selected)
    accuracy = accuracy_score(y_predict, y_test)
    accuracies.append(accuracy)

    if accuracy > max_accuracy2:
        max_accuracy2 = accuracy
        optimal_i = i

print(f"Maximum accuracy is: {max_accuracy2}, Number of K is: {optimal_i} ")

if __name__ == "__main__":
   plt.figure(figsize=(12, 6))
   plt.plot(neighbors, accuracies, marker='o')
   plt.xlabel('Number of Neighbors')
   plt.ylabel('Accuracy')
   plt.title('KNN Accuracy and Number of Neighbors')
   plt.xticks(range(min(neighbors), max(neighbors) + 1, 5))
   plt.grid(True)
   plt.show()
