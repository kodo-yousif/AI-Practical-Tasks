import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import  accuracy_score
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt




class SVM:
    def __init__ (self):
        pass

    def svm_algorithm(data):
        
        # Split into features (X) and labels (y)
        X = data.drop('Dangerous', axis=1)
        y = data['Dangerous']

        over_sampler = RandomOverSampler(random_state=42)
        X, y = over_sampler.fit_resample(X, y) #x and y train are now resampled

        # Split the dataset into a training set and a testing set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


        # Instantiate an SVM classifier
        svm_model = SVC(kernel='sigmoid', C=1.0)
        # the parameter C is a regularization parameter that controls the trade-off between achieving a low training error and a low testing error, smaller softer, larger better job for classification

        # Train the model on the training set
        svm_model.fit(X_train, y_train)

        # Make predictions on the testing set
        y_pred = svm_model.predict(X_test)

        # Evaluate the model's performance
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Accuracy: {accuracy}")

        #  Plot pie charts for predicted and true values
        labels = ['Yes', 'No']

        # For Predicted Values
        plt.subplot(1, 2, 1)
        plt.pie(pd.Series(y_pred).value_counts(), labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f'Predicted Values\nAccuracy: {accuracy*100:.2f}%')

        # For True Values
        plt.subplot(1, 2, 2)
        plt.pie(pd.Series(y_test).value_counts(), labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('True Values')

        plt.show()