import tkinter as tk
from tkinter import ttk
from helpers.widgets import tkInput, tkLabel

# import tkinter as tk
# from tkinter import ttk

class MyApp:
    def __init__(self, master):
        self.master = master
        master.geometry("950x700")
        master.title("Software for Digital Innovation (Madonna Tsegha)")

        # Create a Notebook (Tab Control)
        self.tabControl = ttk.Notebook(master)
        self.phaseOne = tk.Frame(self.tabControl)
        self.phaseTwo = tk.Frame(self.tabControl)

        self.tabControl.add(self.phaseOne, text="Phase One")
        self.tabControl.add(self.phaseTwo, text="Phase Two")
        self.tabControl.pack(expand=1, fill="both")

        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_forms()
        self.create_search_widgets()

    def create_labels(self):
        tk.Label(self.phaseOne, text="This tab shows phase One of the project. Click any of the buttons below to get started", x=0, y=5).pack()
        tk.Label(self.phaseTwo, text="This tab shows the visualization used for Stop and Search API provided by the UK police", x=0, y=5).pack()

    def create_forms(self):
        form = tk.Frame(self.phaseOne, width=500, height=400)
        form.place(x=100, y=120)

        form2 = tk.Frame(self.phaseTwo, width=500, height=400)
        form2.place(x=100, y=50)

    def create_search_widgets(self):
        tk.Label(self.master, text='Enter a city to search:', x=220, y=50).pack()
        self.city_entry = tk.Entry(self.master)
        self.city_entry.insert(0, "Enter a city to search")
        self.city_entry.place(x=380, y=50)
        tk.Button(self.master, text="Search", command=self.search_text).place(x=580, y=50)

    def search_text(self):
        print('Hey, I was clicked')

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()



# def searchText():
#     print('Hey I was clicked')

# def tkinter_app():

#     root = tk.Tk()
#     root.geometry("950x700")
#     root.title("Software for Digital Innovation (Madonna Tsegha)")
    
#     # phase1, phase2, phase3
    
#     tabControl = ttk.Notebook(root)
#     phaseOne = tk.Frame(tabControl)
#     phaseTwo = tk.Frame(tabControl)

#     tabControl.add(phaseOne, text="Phase One")
#     tabControl.add(phaseTwo, text="Phase Two")
#     tabControl.pack(expand=1, fill="both")

#     tkLabel(phaseOne, text="This tab shows phase One of the project. Click any of the buttons below to get started", x=0, y=5)
#     tkLabel(phaseTwo, text="This tab shows the visualization used for Stop and Search api provided by the UK police)", x=0, y=5)
#     form = tk.Frame(phaseOne, width=500, height=400)
#     form.place(x=100, y=120)

#     form2 = tk.Frame(phaseTwo, width=500, height=400)
#     form2.place(x=100, y=50)
    
#     tkLabel(root, text='Enter a city to search:', x=220, y=50)
#     tkInput(root, text="Enter a city to search", x=380, y=50)
#     tk.Button(root, text= "Search", command=lambda: searchText()).place(x=580, y=50) 
    
#     return root

# if __name__ == "__main__":
#     tkinter_app().mainloop()