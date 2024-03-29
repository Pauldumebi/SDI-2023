import tkinter as tk
from helpers.widgets import tk_label
from helpers.utils import database_connection
from tkinter import ttk
from form_1 import PhaseOneForm
from form_2 import PhaseTwoForm
from form_3 import PhaseThreeForm
from phase_4 import PhaseFourForm

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1150x800")
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
        
        if database_connection() is not None:
            self.create_forms()
        else:
            tk_label(self.tabControl, text="No database found please connect a database to continue", x=400, y=150)
            
    def create_forms(self):
        window1 = self.phaseOne
        form = tk.Frame(window1, width=900, height=600)
        form.place(x=50, y=50)

        form2 = tk.Frame(self.phaseTwo, width=950, height=600)
        form2.place(x=100, y=50)
        
        form3 = tk.Frame(self.phaseThree, width=950, height=600)
        form3.place(x=150, y=50)
        
        form4 = tk.Frame(self.phaseFour, width=950, height=600)
        form4.place(x=50, y=50)
        
        form_one_instance = PhaseOneForm()
        form_one_instance.form1(window1, form)
        
        form_two_instance = PhaseTwoForm()
        form_two_instance.form2(form2)
        
        form_three_i