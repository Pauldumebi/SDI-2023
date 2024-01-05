from helpers.widgets import tk_input, tk_label

class PhaseThreeForm:
    # def __init__(self):
    #     self.phaseThree = ''
        
    def form3(self, form):
        if len(form.winfo_children()) > 0:
            for widget in form.winfo_children():
                widget.destroy()
                
        
        tk_label(form, text="This tab shows Phase Three of the project. Click any of the buttons below to get started", x=0, y=5)
        tk_label(form, text='This is form 3', x=0, y=80)
    