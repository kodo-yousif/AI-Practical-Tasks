import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.ensemble import RandomForestClassifier

path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Re-creating the training and test splits without standardizing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Using Random Forest to determine feature importance
rf = RandomForestClassifier(n_estimators=150, random_state=42)
rf.fit(X_train, y_train)
feature_importances = rf.feature_importances_

# Ranking the features by importance
feature_importance_ranking = pd.Series(feature_importances, index=X_train.columns).sort_values(ascending=False)

accuracies = []
selected_feature_sets = []

for i in range(1, len(feature_importance_ranking) + 1):

    selected_features_indices = np.argsort(feature_importances)[-i:]
    X_train_selected = X_train.iloc[:, selected_features_indices]
    X_test_selected = X_test.iloc[:, selected_features_indices]

    # Training the SVM classifier
    svm_selected = SVC(kernel='poly')
    svm_selected.fit(X_train_selected, y_train)

    # Predicting the test set results
    y_pred_selected = svm_selected.predict(X_test_selected)

    # Calculating accuracy
    accuracy_selected = accuracy_score(y_test, y_pred_selected)

    # Storing results
    accuracies.append(accuracy_selected)
    selected_feature_sets.append(X_train.columns[selected_features_indices].tolist())

# Combine the results for analysis
results = pd.DataFrame({
    'Number of Features': range(1, len(feature_importance_ranking) + 1),
    'Selected Features': selected_feature_sets,
    'Accuracy': accuracies
})

FinalResult = results.sort_values(by='Accuracy', ascending=False)


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RandomForest Feature Selection Results</title>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>RandomForest Feature Selection Results-poly</h1>
    {}
</body>
</html>
"""

# Insert the HTML table into the template
html_content = html_content.format(FinalResult.to_html(index=False))

with open("svm_randomForest_poly.html", "w") as html_file:
    html_file.write(html_content)

results_of_high_accuracy=max(accuracies)
print(f'maximum accuracy = {results_of_high_accuracy}')
