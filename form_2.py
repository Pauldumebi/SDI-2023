from helpers.widgets import tk_input, tk_label

class PhaseTwoForm:
    # def __init__(self):
    #     self.phaseTwo = ''
        
    def form2(self, form):
        if len(form.winfo_children()) > 0:
            for widget in form.winfo_children():
                widget.destroy()
                
                
        tk_label(form, text="This tab shows Phase Two of the project. Click any of the buttons below to get started", x=0, y=5)
        tk_input(form, text='This is form 2', x=0, y=80)
                
