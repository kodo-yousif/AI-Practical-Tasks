from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import tkinter as tk
from tkinter import ttk
import pandas as pd


class FeatureImportance:
    def __init__():
        pass
    def feature_importance( data):
            
        X_train = data.drop('Dangerous', axis=1)
        y_train = data['Dangerous']
        # Fit the model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Get feature importances
        feature_importances = model.feature_importances_


        # Reverse the feature importance scores back to the original feature names
        feature_names = X_train.columns.tolist()

        # Create a dictionary mapping feature names to their importance scores
        feature_importance_dict = dict(zip(feature_names, feature_importances))

        # Sort the features based on their importance scores (optional)
        sorted_features = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

        accuracy = 0
        # Print or use the sorted features
        for feature, importance in sorted_features:
            print(f"{feature}: {importance}")
            accuracy = accuracy + importance

        # Alternatively, if you want to access the importance of a specific feature:
        desired_feature = 'symptoms4_Lip'
        importance_of_desired_feature = feature_importance_dict.get(desired_feature, None)
        print(f"Importance of {desired_feature}: {importance_of_desired_feature}")
        print('and also the accuracy is ', accuracy)


        # Create a DataFrame with feature names and their importances
        feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': feature_importances})

        # Sort the DataFrame by Importance in descending order
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

        # Get the top five features
        top_fifteen_features = feature_importance_df.head(15)

        print("Top fifteen features:")
        print(top_fifteen_features)



        def display_top_features():
            result_text.delete(1.0, tk.END)  # Clear previous content
            result_text.insert(tk.END, "Top Fifteen Features:\n" + str(top_fifteen_features * 100))

        def display_all_features():
            result_text.delete(1.0, tk.END)  # Clear previous content
            result_text.insert(tk.END, "All Features:\n" + str(feature_importance_df * 100))

        def display_accuracy():
            result_text.delete(1.0, tk.END)  # Clear previous content
            result_text.insert(tk.END, "Accuracy: " + str(accuracy * 100))

        def display_desired_feature():
            result_text.delete(1.0, tk.END)  # Clear previous content
            importance_of_desired_feature = feature_importance_dict.get(desired_feature_var.get(), None)
            result_text.insert(tk.END, f"Importance of {desired_feature_var.get()}: {importance_of_desired_feature * 100}")


        # GUI
        root = tk.Tk()
        root.title("Feature Importance Viewer")

        # Buttons
        top_features_button = ttk.Button(root, text="Show Top Features", command=display_top_features)
        top_features_button.pack(pady=10)

        all_features_button = ttk.Button(root, text="Show All Features", command=display_all_features)
        all_features_button.pack(pady=10)

        accuracy_button = ttk.Button(root, text="Show Accuracy", command=display_accuracy)
        accuracy_button.pack(pady=10)

        # Entry for selecting desired feature
        desired_feature_var = tk.StringVar()
        desired_feature_entry = ttk.Entry(root, textvariable=desired_feature_var)
        desired_feature_entry.pack(pady=10)

        desired_feature_button = ttk.Button(root, text="Show Desired Feature", command=display_desired_feature)
        desired_feature_button.pack(pady=10)

        # Text widget to display results
        result_text = tk.Text(root, height=10, width=70)
        result_text.pack(pady=10)

        root.mainloop()