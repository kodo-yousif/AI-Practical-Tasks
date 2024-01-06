import tkinter as tk
import tkinter.font as tkFont
import subprocess

class App:
    def __init__(self, root):
        # Setting title and size
        root.title("SVM")
        width = 303
        height = 600  # Increased height to accommodate all buttons
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Common button font and style
        ft = tkFont.Font(family='Times', size=10)
        button_bg = "#c0c0c0"
        button_fg = "#000000"

        # Function to create a button
        def create_button(text, command, y_position):
            button = tk.Button(root, text=text, command=command, bg=button_bg, fg=button_fg, font=ft)
            button.place(x=50, y=y_position, width=204, height=45)
            return button

        # Create buttons
        GButton_747 = create_button("SVM Radial Basis Function", self.GButton_747_command, 50)
        GButton_13 = create_button("SVM Polynomial", self.GButton_13_command, 110)
        GButton_678 = create_button("SVM Standard scaler Confusion Matrix", self.GButton_678_command, 170)
        GButton_643 = create_button("SVM Standard scaler Fselection f_classif", self.GButton_643_command, 230)
        GButton_642 = create_button("SVM RandomForest Polynomial", self.GButton_642_command, 290)
        GButton_641 = create_button("SVM RandomForest Radial Basis Function", self.GButton_641_command, 350)
        GButton_640 = create_button("SVM Fselection", self.GButton_640_command, 410)
        GButton_639 = create_button("SVM Plot", self.GButton_639_command, 470)
        GButton_638 = create_button("SVM Linear Support Vector Classification", self.GButton_638_command, 530)

        # Title label
        GLabel_658 = tk.Label(root, font=tkFont.Font(family='Times', size=18), fg="#333333", text="Support Vector Machine")
        GLabel_658.place(x=25, y=10, width=230, height=45)

    def GButton_747_command(self):
        subprocess.run(["python", "svm_rbf.py"], check=True)


    def GButton_13_command(self):
        subprocess.run(["python", "svm_poly.py"], check=True)
        


    def GButton_678_command(self):
        subprocess.run(["python", "svm_standardscaler_confusionmatrix.py"], check=True)


    def GButton_643_command(self):
        subprocess.run(["python", "svm_standardscaler_fselection.py"], check=True)

    def GButton_642_command(self):
        subprocess.run(["python", "svm_randomForest_poly.py"], check=True)
        
    def GButton_641_command(self):
        subprocess.run(["python", "svm_randomForest_rbf.py"], check=True)
    
    def GButton_640_command(self):
        subprocess.run(["python", "svm_fselection.py"], check=True)
    
    def GButton_639_command(self):
        subprocess.run(["python", "svm_Plot.py"], check=True)

    def GButton_638_command(self):
        subprocess.run(["python", "svm_linearSVC.py"], check=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
