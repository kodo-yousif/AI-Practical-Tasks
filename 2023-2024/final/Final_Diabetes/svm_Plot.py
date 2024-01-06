import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
path = 'dataset.csv'
load_dataset = pd.read_csv(path)
X, y = load_dataset.drop('Outcome', axis=1), load_dataset['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# PCA for visualization
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Plotting the PCA-transformed features
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_train_pca[:, 0], y=X_train_pca[:, 1], hue=y_train)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Features')
plt.legend()
plt.show()

# Feature selection for model training
selector = SelectKBest(f_classif, k=2)  
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

# Training the SVM classifier on the selected features
svm = SVC(kernel='rbf')
svm.fit(X_train_selected, y_train)

# Predicting the test set results
y_pred = svm.predict(X_test_selected)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Optional: Print the selected features
selected_features = load_dataset.columns[selector.get_support(indices=True)]
print('Selected Features:', selected_features.tolist())
