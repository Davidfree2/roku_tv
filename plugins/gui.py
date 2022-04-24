import tkinter as tk




class Gui:
    def __init__(self, window):
        self.window = window
        self.title = self.window.title("h")
        self.frame = tk.Frame(self.window)

        self.button = tk.Button(self.frame, text='hello')
        self.button.pack()
        self.frame.pack()





root = tk.Tk()
app = Gui(root)
root.mainloop()
