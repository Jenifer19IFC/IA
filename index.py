import tkinter as tk
from Interface.Interface import Interface

class Index:
    def __init__(self):
        self.root = tk.Tk()
        self.interface = Interface(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    index = Index()
    index.run()
