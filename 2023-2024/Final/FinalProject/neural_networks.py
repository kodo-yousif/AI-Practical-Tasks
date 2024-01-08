import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from imblearn.over_sampling import RandomOverSampler
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


class NN:
    def __init__ (self):
        pass

    def neural_networks_algorithm(data):

        # Split into features (X) and labels (y)
        X = data.drop('Dangerous', axis=1)
        y = data['Dangerous']
            
        
        # under_sampler = NearMiss(version=1, sampling_strategy='auto')
        over_sampler = RandomOverSampler(random_state=42)
        X, y = over_sampler.fit_resample(X, y) #x and y train are now resampled

        # Step 2: Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Neural NetworkAlgorithm:
        # Step 3: Build the Neural Network Model
        model = Sequential()
        # dense: fully connected
        model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
        # .shape[1]: For example, if X_train is a 2D array with shape (100, 10), where 100 is the number of samples (rows) and 10 is the number of features (columns), then X_train.shape[1] would be 10.
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # Compile the model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # The choice of loss function defines the objective that the model will try to minimize during training.

        # Step 4: Train the Neural Network Model
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

        # Step 5: Evaluate the Model
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

        # Step 6: Make Predictions
        y_pred = model.predict(X_test)
        y_pred_classes = np.round(y_pred)

        # Step 7: Confusion Matrix
        # Calculate Confusion Matrix
        cm = confusion_matrix(y_test, y_pred_classes)


        # Access the elements of the confusion matrix
        TN = cm[0, 0]
        FP = cm[0, 1]
        FN = cm[1, 0]
        TP = cm[1, 1]

        # You can print these values to see the counts
        print("True Negative (TN):", TN)
        print("False Positive (FP):", FP)
        print("False Negative (FN):", FN)
        print("True Positive (TP):", TP)
 

        # Plot Confusion Matrix
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
        plt.title(f'Confusion Matrix - Predicted vs Actual\nAccuracy: {accuracy*100:.2f}%')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.show()