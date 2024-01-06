from Bayesian import accuracy_gnb1
from Bayesian_fselection_fclassif import accuracy_gnb2
from Bayesian_standardscaler_fselection_fclassif import accuracy_gnb3
from Bayesian_standardscaler_fselection_mutualclassif import accuracy_gnb4
from KNN_fselection_fclassif import max_accuracy1
from KNN_fselection_mutualclassif import max_accuracy2
from KNN_randomforest import max_accuracy3
from KNN import max_accuracy4
from MLP_fselection_relu import Max_acc1
from MLP_fselection_sigmoid import Max_acc2
from MLP_relu import Max_acc3
from MLP_sig import Max_acc4
from MLP_standardscaler_classifrepo import accuracy1
from svm_fselection import accuracy_selected1
from svm_linearSVC import accuracy_selected2
from svm_randomForest_poly import results_of_high_accuracy
from svm_randomForest_rbf import high_accuracy
from svm_standardscaler_confusionmatrix import accuracy2
from svm_standardscaler_fselection import accuracy_selected1
from svm_rbf import accuracy_selected2
from svm_poly import accuracy_selected3
import matplotlib.pyplot as plt

accuracies =  [accuracy_gnb1, accuracy_gnb2, accuracy_gnb3, accuracy_gnb4, max_accuracy1, max_accuracy2, max_accuracy3, max_accuracy4,Max_acc1,Max_acc2,Max_acc3,Max_acc4,accuracy1,accuracy_selected1,accuracy_selected2,results_of_high_accuracy,high_accuracy,accuracy2,accuracy_selected1,accuracy_selected2,accuracy_selected3]
classifiers = ["Bayesian", "Bayesian_fclassif", "Bayesian_standardScaler_fclassif", "Bayesian_standardScaler_mutualclassif", "KNN_fclassif", "KNN_mutualclassif", "KNN_randomforest", "KNN","MLP_mutualclassif_relu","MLP_mutualclassif_sigmoid","MLP_relu","MLP_sigmoid","MLP_standardscaler_classifRepo","SVM_f_classif","SVM_linearSVC","SVM_radndomForest_poly","SVM_radndomForest_rbf","SVM_strandardscaler_rbf","SVM_strandardscaler_fselection_rbf","SVM_rbf","SVM_poly"]

plt.figure(figsize=(18, 6))
plt.plot(classifiers, accuracies, marker="o")
plt.xlabel("Classifiers")
plt.ylabel("Accuracy")
plt.title("Comparison of Accuracy")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(True)
plt.show()
