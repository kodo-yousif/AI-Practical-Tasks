import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV




class KNN:

    def __init__ (self):
        pass
    
    def knn_algorithm(data):

        # # Split into features (X) and labels (y)
        X = data.drop('Dangerous', axis=1) #for column
        y = data['Dangerous']
       
        under_sampler = RandomOverSampler(random_state=42)
        X, y = under_sampler.fit_resample(X, y) #x and y train are now resampled

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        # har jaraw bashek warbgra pashan lasar hamuy kar bka.


        # step 3: find the optimal k
        # Perform a grid search to find the optimal number of neighbors
        param_grid = {'n_neighbors': list(range(1, 21))}
        knn = KNeighborsClassifier()
        grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)

        # Get the optimal value of n_neighbors
        optimal_k = grid_search.best_params_['n_neighbors']
        print(f"The optimal number of neighbors is: {optimal_k}")

        # Step 4: Train the KNN Model
        knn_model = KNeighborsClassifier(n_neighbors=optimal_k)  # Use an appropriate value for 'n_neighbors', use the optimal k value.
        knn_model.fit(X_train, y_train)

        # Step 5: Make Predictions
        y_pred = knn_model.predict(X_test)

        # Step 6: Evaluate the Model
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Accuracy: {accuracy}')

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