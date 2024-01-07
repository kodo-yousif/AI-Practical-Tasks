import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# Load the Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()

data = pd.DataFrame(data=np.c_[iris['data']],
                    columns=iris['feature_names'])

# Predict Sepal Width based on Sepal Length

print(data)
sepal_length = data[['sepal length (cm)']]

sepal_width = data[['sepal width (cm)']]


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    sepal_length, sepal_width, test_size=0.8, random_state=0)

# Create a linear regression model for Sepal Width prediction
model_sepal_width = LinearRegression()

model_sepal_width.fit(X_train, y_train)
# Make predictions on the test data
y_pred_sepal_width = model_sepal_width.predict(X_test)
# Evaluate the model for Sepal Width prediction
r2_sepal_width = r2_score(y_test, y_pred_sepal_width)
print(y_test)
print(y_pred_sepal_width)
print(
    f'R-squared for Sepal Width prediction based on sepal length: {r2_sepal_width:.2f}')


# Predict Petal Length based on Sepal Length and Sepal Width
sepal_length_width = data[['sepal length (cm)', 'sepal width (cm)']]

petal_length = data['petal length (cm)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    sepal_length_width, petal_length, test_size=0.2, random_state=42)

# Create a linear regression model for Petal Length prediction
model_petal_length = LinearRegression()
model_petal_length.fit(X_train, y_train)

# Make predictions on the test data
y_pred_petal_length = model_petal_length.predict(X_test)

# Evaluate the model for Petal Length prediction
r2_petal_length = r2_score(y_test, y_pred_petal_length)
print(f'R-squared for Petal Length prediction: {r2_petal_length:.2f}')


# Predict Petal Width based on Sepal Length, Sepal Width
petal_width = data['petal width (cm)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    sepal_length_width, petal_width, test_size=0.2, random_state=42)

# Create a linear regression model for Petal Width prediction
model_petal_width = LinearRegression()
model_petal_width.fit(X_train, y_train)

# Make predictions on the test data
y_pred_petal_width = model_petal_width.predict(X_test)

# Evaluate the model for Petal Width prediction
r2_petal_width = r2_score(y_test, y_pred_petal_width)
print(f'R-squared for Petal Width prediction: {r2_petal_width:.2f}')

print(sepal_length_width)