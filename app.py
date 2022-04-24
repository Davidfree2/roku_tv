import tkinter as tk
from plugins.roku import Roku
from plugins.gui import Gui




def main():

    my_device = Roku("192.168.1.64", "8060")

    root = tk.Tk()
    app = Gui(root, my_device)
    root.mainloop()




main()
