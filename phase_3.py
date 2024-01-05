import tkinter as tk
from helpers.widgets import tk_input, tk_label
from tkinter import ttk
from form_1 import PhaseOneForm
from form_2 import PhaseTwoForm
from form_3 import PhaseThreeForm
from form_4 import PhaseFourForm

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x800")
        self.title("Software for Digital Innovation (Madonna Tsegha)")

        self.tabControl = ttk.Notebook(self)
        self.phaseOne = tk.Frame(self.tabControl)
        self.phaseTwo = tk.Frame(self.tabControl)
        self.phaseThree = tk.Frame(self.tabControl)
        self.phaseFour = tk.Frame(self.tabControl)

        self.tabControl.add(self.phaseOne, text="Phase One")
        self.tabControl.add(self.phaseTwo, text="Phase Two")
        self.tabControl.add(self.phaseThree, text="Phase Three")
        self.tabControl.add(self.phaseFour, text="Phase Four")
        self.tabControl.pack(expand=1, fill="both")
        
        self.create_forms()

    def create_forms(self):
        window1 = self.phaseOne
        form = tk.Frame(window1, width=900, height=400)
        form.place(x=50, y=50)

        form2 = tk.Frame(self.phaseTwo, width=600, height=400)
        form2.place(x=150, y=50)
        
        form3 = tk.Frame(self.phaseThree, width=600, height=400)
        form3.place(x=150, y=50)
        
        form4 = tk.Frame(self.phaseFour, width=600, height=400)
        form4.place(x=150, y=50)
        
        form_one_instance = PhaseOneForm()
        form_one_instance.form1(window1, form)
        
        form_two_instance = PhaseTwoForm()
        form_two_instance.form2(form2)
        
        form_three_instance = PhaseThreeForm()
        form_three_instance.form3(form3)
        
        form_four_instance = PhaseFourForm()
        form_four_instance.form4(form4)


if __name__ == "__main__":
    root = MyApp()
    root.mainloop()