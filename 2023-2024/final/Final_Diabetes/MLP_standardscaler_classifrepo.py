import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import tkinter as tk
from tkinter import ttk

# Load the dataset
path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create an MLPClassifier model
mlp = MLPClassifier(hidden_layer_sizes=(20,5), activation='relu',
                    max_iter=1000, random_state=42)

# Train the model on the training data
mlp.fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred = mlp.predict(X_test_scaled)
Traing_test=mlp.score(X_train,y_train)
Test_set_test=mlp.score(X_test,y_test)
# Calculate the accuracy of the model
accuracy1 = accuracy_score(y_test, y_pred)
print(f" Accuracy: {accuracy1:.2f}")
print(f"Trainig test score is :{Traing_test}")
print(f"Testing test score is :{Test_set_test}")

# Generate and display the classification report
class_report = classification_report(y_test, y_pred,output_dict=True)

# Function to display the classification report in a GUI table
def display_report_gui(report):
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Classification Report")

    # Create a Treeview widget
    tree = ttk.Treeview(window, columns=('precision', 'recall', 'f1-score', 'support'), show='headings')

    # Define headings
    tree.heading('precision', text='Precision')
    tree.heading('recall', text='Recall')
    tree.heading('f1-score', text='F1-Score')
    tree.heading('support', text='Support')

    # Inserting data into the Treeview widget
    for class_name, metrics in report.items():
        if class_name not in ('accuracy', 'macro avg', 'weighted avg'):
            tree.insert('', tk.END, values=(metrics['precision'], metrics['recall'], metrics['f1-score'], metrics['support']))

    # Add treeview to the window and run the GUI
    tree.pack(expand=True, fill='both')
    window.mainloop()


if __name__ == "__main__":
# Display the classification report in a GUI
  display_report_gui(class_report)