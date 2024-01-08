import pandas as pd
from fancyimpute import IterativeImputer
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from knn import KNN
from svm import SVM
from bayesian_classifier import BayesianClassifier
from neural_networks import NN
from feature_importance import FeatureImportance

class AnimalCondition:
    def __init__(self, data):
        self.data = data

    
    def get_null_vals( self, feature ):
        # get the null values
        null_vals = self.data[ self.data[ feature ].isnull()]
        return null_vals
        # get the null values in the dataset.


    def missing_imputations(self ):

        self.null_vals_before_imputation = self.get_null_vals( 'Dangerous')

        categorical_columns = [col for col in self.data.select_dtypes(include=['object']).columns if col != 'Dangerous']

        label_mapping = {}

        for col in categorical_columns:
            labels, unique_values = pd.factorize(self.data[col])
            label_mapping[col] = dict(zip(unique_values, labels))

        # Apply manual encoding to categorical columns
        for col in categorical_columns:
            if col != 'Dangerous':
                self.data[col] = self.data[col].map(label_mapping[col])


        self.data['Dangerous'] = self.data['Dangerous'].map({'Yes': 1, 'No': 0})

        # Apply MICE imputation
        imputer = IterativeImputer()
        data_imputed = imputer.fit_transform(self.data)


        # Convert the imputed data array back to a DataFrame
        data_imputed = pd.DataFrame(data_imputed, columns=self.data.columns)


        data_imputed['Dangerous'] = data_imputed['Dangerous'].round().astype(int)

        # Reverse the encoding for 'Dangerous' column
        data_imputed['Dangerous'] = data_imputed['Dangerous'].map({1: 'Yes', 0: 'No'})


        # Reverse the encoding for categorical columns
        for col in categorical_columns:
            if col != 'Dangerous':
                data_imputed[col] = data_imputed[col].map({i: value for value, i in label_mapping[col].items()})
                self.data[col] = self.data[col].map({i: value for value, i in label_mapping[col].items()})

        self.data = data_imputed
        self.null_vals_after_imputation = self.get_null_vals('Dangerous')

        
        return data_imputed

    def one_hot_encoding( self):
        # Step 1: Data Preprocessing
        # Convert categorical variables to numerical values
        data_numeric = pd.get_dummies(self.data, columns=self.data.select_dtypes(include=['object']).columns)

        # Create a new column 'Dangerous' based on conditions
        data_numeric['Dangerous'] = 0  # Initialize with 0
        data_numeric.loc[data_numeric['Dangerous_Yes'] == 1, 'Dangerous'] = 1

        # Drop the original columns 'Dangerous_Yes' and 'Dangerous_No'
        data_numeric = data_numeric.drop(['Dangerous_Yes', 'Dangerous_No'], axis=1)

        self.data = data_numeric        


    # Feature Importance
    def feature_importance( self):
        FeatureImportance.feature_importance( self.data)

    #Algorithms
    def knn(self ):
        KNN.knn_algorithm( self.data)

    def svm(self ):
        SVM.svm_algorithm( self.data)

    def bayesian_classifier(self ):
        BayesianClassifier.bayesian_classifier_algorithm( self.data)

    def neural_networks(self ):
        NN.neural_networks_algorithm( self.data)

class AnimalConditionGUI:
    def __init__(self, root, obj):
        self.root = root
        self.root.title("Animal Condition GUI")

        # Create a Frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create a scrolled text widget to display the result
        self.result_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=140, height=10)
        self.result_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create a button to trigger the action
        self.show_button = ttk.Button(self.frame, text="Show Missing Values", command=self.show_null_values)
        self.show_button.grid(row=1, column=0, pady=10)

        self.show_solved_button = ttk.Button(self.frame, text="Show Solved Values", command=self.show_solved_values)
        self.show_solved_button.grid(row=1, column=1, pady=10)

        # Store the AnimalCondition instance
        self.obj = obj

    def show_null_values(self):
        feature = 'Dangerous'
        null_vals = self.obj.get_null_vals( feature)
        self.result_text.delete(1.0, tk.END)  # Clear previous text
        self.result_text.insert(tk.END, null_vals)

    def show_solved_values(self):
            data_imputed = self.obj.missing_imputations()
            if self.obj.null_vals_before_imputation is not None and self.obj.null_vals_after_imputation is not None:
                before_imputation = self.obj.null_vals_before_imputation
                after_imputation = self.obj.null_vals_after_imputation

                self.result_text.delete(1.0, tk.END)  # Clear previous text
                self.result_text.insert(tk.END, "Null Values Before Imputation:\n")
                self.result_text.insert(tk.END, str(before_imputation) + "\n\n")

                self.result_text.insert(tk.END, "Null Values After Imputation:\n")
                self.result_text.insert(tk.END, str(after_imputation))


#get the data from csv file
path = "C:\\Users\\Saif Service Center\\Desktop\\year4\\ZhyaRebwar-Semester1\\Software\\AI\\FinalProject\\archive\\data.csv"
file_csv = open(path, "r") #r for read
# Assuming 'data' is your DataFrame containing the dataset
data = pd.read_csv(file_csv)
feature = 'Dangerous'

obj = AnimalCondition(data=data)
# obj.missing_imputations()
# obj.one_hot_encoding()

# obj.feature_importance()


# obj.knn() # for knn
# obj.svm() # for svm
# obj.bayesian_classifier() # for bayesian classifier
# obj.neural_networks() # for neural networks


# # Create the Tkinter root window
# root = tk.Tk()

# # Create the GUI instance
# gui = AnimalConditionGUI(root, obj)

# # Start the Tkinter event loop
# root.mainloop()