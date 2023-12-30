from helpers.widgets import tkInput, tkLabel

class PhaseFourForm:
    # def __init__(self):
    #     self.phaseThree = ''
        
    def form4(self, form):
        if len(form.winfo_children()) > 0:
            for widget in form.winfo_children():
                widget.destroy()
                
        
        tkLabel(form, text="This tab shows Phase Four of the project. Click any of the buttons below to get started", x=0, y=5)
        tkLabel(form, text='This is form 4', x=0, y=80)
                