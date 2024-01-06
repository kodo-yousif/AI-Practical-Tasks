import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


path='dataset.csv'
load_dataset=pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Apply Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)
accuracy_gnb1 = accuracy_score(y_test, y_pred_gnb)
Traing_test=gnb.score(X_train,y_train)
Test_set_test=gnb.score(X_test,y_test)
print(f"Gaussian Naive Bayes Accuracy: {accuracy_gnb1}")
print(f"Trainig test score is :{Traing_test}")
print(f"Testing test score is :{Test_set_test}")


