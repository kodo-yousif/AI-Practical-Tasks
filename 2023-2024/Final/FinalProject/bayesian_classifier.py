import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt



class BayesianClassifier:
    def __init__ (self ):
        pass

    def bayesian_classifier_algorithm( data):

        # Convert categorical features to numerical using LabelEncoder
        label_encoder = LabelEncoder()
        df_encoded = data.apply(label_encoder.fit_transform)

        # Split the dataset into features (X) and target variable (y)
        X = df_encoded.drop('Dangerous', axis=1)  # Features
        y = df_encoded['Dangerous']  # Target variable

        # under_sampler = NearMiss(version=1, sampling_strategy='auto') # RandomUnderSampler(random_state=42)
        over_sampler = RandomOverSampler(random_state=42)
        X, y = over_sampler.fit_resample(X, y) #x and y train are now resampled

        # Split the data into a training set (80%) and a testing set (20%)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Use a Multinomial Naive Bayes classifier
        model = MultinomialNB()
        # The "Multinomial" part indicates that the features are assumed to be discrete, typically representing counts

        # Train the model
        model.fit(X_train, y_train)

        # Predict on the testing set
        y_pred = model.predict(X_test)
        # print( y_pred) 

        # Evaluate the performance
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")

       # Plot the cross-validated accuracy for different values of K
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