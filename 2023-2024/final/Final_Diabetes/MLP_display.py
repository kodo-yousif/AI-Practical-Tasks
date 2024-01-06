import tkinter as tk
import tkinter.font as tkFont
import subprocess
class App:
    def __init__(self, root):
        #setting title
        root.title("MLP")
        width=303
        height=475
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_747=tk.Button(root)
        GButton_747["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_747["font"] = ft
        GButton_747["fg"] = "#000000"
        GButton_747["justify"] = "center"
        GButton_747["text"] = "MLP Rectified Linear Unit"
        GButton_747.place(x=70,y=60,width=148,height=42)
        GButton_747["command"] = self.GButton_747_command

        GButton_13=tk.Button(root)
        GButton_13["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_13["font"] = ft
        GButton_13["fg"] = "#000000"
        GButton_13["justify"] = "center"
        GButton_13["text"] = "MLP sigmoid or Logistic"
        GButton_13.place(x=70,y=140,width=146,height=45)
        GButton_13["command"] = self.GButton_13_command

        GButton_678=tk.Button(root)
        GButton_678["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_678["font"] = ft
        GButton_678["fg"] = "#000000"
        GButton_678["justify"] = "center"
        GButton_678["text"] = "MLP Fselection Standard scaler classifrepo"
        GButton_678.place(x=50,y=225,width=204,height=43)
        GButton_678["command"] = self.GButton_678_command

        GButton_643=tk.Button(root)
        GButton_643["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_643["font"] = ft
        GButton_643["fg"] = "#000000"
        GButton_643["justify"] = "center"
        GButton_643["text"] = "MLP Fselection RELU"
        GButton_643.place(x=50,y=300,width=204,height=45)
        GButton_643["command"] = self.GButton_643_command
        
        GButton_642=tk.Button(root)
        GButton_642["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_642["font"] = ft
        GButton_642["fg"] = "#000000"
        GButton_642["justify"] = "center"
        GButton_642["text"] = "MLP Fselection Sigmoid"
        GButton_642.place(x=50,y=390,width=204,height=45)
        GButton_642["command"] = self.GButton_642_command


        GLabel_658=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_658["font"] = ft
        GLabel_658["fg"] = "#333333"
        GLabel_658["justify"] = "center"
        GLabel_658["text"] = "Multilayer Perceptron "
        GLabel_658.place(x=40,y=10,width=230,height=56)

    def GButton_747_command(self):
        subprocess.run(["python", "MLP_relu.py"], check=True)


    def GButton_13_command(self):
        subprocess.run(["python", "MLP_sig.py"], check=True)
        


    def GButton_678_command(self):
        subprocess.run(["python", "MLP_standardscaler_classifrepo.py"], check=True)


    def GButton_643_command(self):
        subprocess.run(["python", "MLP_fselection_relu.py"], check=True)

    def GButton_642_command(self):
        subprocess.run(["python", "MLP_fselection_sigmoid.py"], check=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
