import pandas as pd
import tkinter as tk
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Load dataset and preprocess
path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardizing the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training the SVM classifier
svm_model = SVC(kernel='rbf')
svm_model.fit(X_train_scaled, y_train)

# Predicting the test set results and calculating accuracy
y_pred = svm_model.predict(X_test_scaled)
accuracy2 = accuracy_score(y_test, y_pred)
print("SVM Model Accuracy:", accuracy2)

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

def display_confusion_matrix(conf_matrix):
    # Root window
    root = tk.Tk()
    root.title("SVM Confusion Matrix Display")

    # Frame for confusion matrix display
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)

    # Creating a matplotlib figure for the confusion matrix
    fig, ax = plt.subplots()
    cax = ax.matshow(conf_matrix, cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    fig.colorbar(cax)
    for (i, j), val in np.ndenumerate(conf_matrix):
        ax.text(j, i, f'{val}', ha='center', va='center')

    # Embedding the matplotlib figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    root.mainloop()

if __name__ == "__main__":
    display_confusion_matrix(conf_matrix)
