import tkinter as tk


class Gui:
    def __init__(self, window, device):
        self.window = window
        self.title = self.window.title("Roku Remote")
        self.frame = tk.Frame(self.window)

        self.device = device

        self.left = tk.Button(self.frame, text='left', command=self.device.left)
        self.right = tk.Button(self.frame, text='right',command=self.device.right)
        self.up = tk.Button(self.frame, text='up', command=self.device.up)
        self.down = tk.Button(self.frame, text='down', command=self.device.down)
        self.home = tk.Button(self.frame, text='home', command=self.device.roku_home)
        self.rev = tk.Button(self.frame, text='reverse', command=self.device.reverse)
        self.forward = tk.Button(self.frame, text='forward', command=self.device.fast_forward)
        self.select = tk.Button(self.frame, text='select', command=self.device.select)

        self.up.grid(row=0, columnspan=2, pady=10, ipady=20, ipadx=20)
        self.left.grid(row=1)
        self.right.grid(row=1, column=1)
        self.down.grid(row=2, columnspan=2, pady=10)
        self.home.grid(row=4, columnspan=2, pady=10)
        self.rev.grid(row=3, column=0, pady=15)
        self.forward.grid(row=3, column=1)
        self.select.grid(row=5, columnspan=2, pady=10)

        self.frame.pack(expand=True)






#root = tk.Tk()
#app = Gui(root, my_device)
#root.mainloop()
