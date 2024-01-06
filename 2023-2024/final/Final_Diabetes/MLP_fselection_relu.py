# Import necessary libraries
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, mutual_info_classif
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
path = "dataset.csv"
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop("Outcome", axis=1), load_dataset["Outcome"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature Selection
fs = SelectKBest(mutual_info_classif, k=4)
fs.fit(X_train, y_train)
X_train_fs = fs.transform(X_train)
X_test_fs = fs.transform(X_test)
selected_feat = fs.get_support()
selected = X.columns[selected_feat]
print(f"Selected Features: {selected}")


# store accuracies
accuracies = []
# node size for each hidden layer
hidden_layers_configurations = [20, 3, 10, 8, 15]
Max_acc1 = 0

# Loop over different hidden layer
for i in range(1, 6):
    num_nodes = hidden_layers_configurations[i - 1]
    # Create an MLPClassifier model
    hidden_layer_sizes = (num_nodes,)
    mlp = MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes,
        activation="relu",
        max_iter=1000,
        random_state=42,
    )

    # Train the model on the training data
    mlp.fit(X_train_fs, y_train)

    # Make predictions on the test data
    y_pred = mlp.predict(X_test_fs)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)

    if accuracy > Max_acc1:
        Max_acc1 = accuracy

    accuracies.append(accuracy)
    print(f"Hidden Layer: {i}, Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 6), accuracies, marker="o")
    plt.title("Accuracy for Different Numbers of Hidden Layers")
    plt.xlabel("Number of Hidden Layers")
    plt.ylabel("Accuracy")
    plt.xticks(range(1, 6))
    plt.show()
    # Creating and displaying a correlation matrix
    correlation_matrix = load_dataset.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix of the Dataset")
    plt.show()
