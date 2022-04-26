import tkinter as tk


class Gui:
    def __init__(self, window, device):
        self.window = window
        self.title = self.window.title("Roku Remote")
        self.frame = tk.Frame(self.window, bg='white')

        self.device = device

        self.left = tk.Button(self.frame, text='left', command=self.device.left)
        self.right = tk.Button(self.frame, text='right',command=self.device.right)
        self.up = tk.Button(self.frame, text='up', command=self.device.up)
        self.down = tk.Button(self.frame, text='down', command=self.device.down)
        self.home = tk.Button(self.frame, text='home', command=self.device.roku_home)
        self.rev = tk.Button(self.frame, text='reverse', command=self.device.reverse)
        self.forward = tk.Button(self.frame, text='forward', command=self.device.fast_forward)
        self.select = tk.Button(self.frame, text='select', command=self.device.select)

        self.volume_up = tk.Button(self.frame, text='volume up', command=self.device.roku_volume_up)
        self.volume_down = tk.Button(self.frame, text='volume down', command=self.device.roku_volume_down)
        self.mute = tk.Button(self.frame, text='mute', command=self.device.roku_mute_unmute)

        self.back = tk.Button(self.frame, text='back', command=self.device.back)

        self.up.grid(row=0, columnspan=2, pady=10, ipady=20, ipadx=20)
        self.left.grid(row=1,  pady=10, ipady=20, ipadx=20)
        self.right.grid(row=1, column=1, pady=10, ipady=20, ipadx=20)
        self.down.grid(row=2, columnspan=2,  pady=10, ipady=20, ipadx=20)
        self.home.grid(row=4, columnspan=2,  pady=10, ipady=20, ipadx=20)
        self.rev.grid(row=3, column=0,  pady=10, ipady=20, ipadx=20)
        self.forward.grid(row=3, column=1,  pady=10, ipady=20, ipadx=20)
        self.select.grid(row=5, columnspan=2,  pady=10, ipady=20, ipadx=20)

        self.volume_up.grid(row=6, column=0,  pady=10, ipady=20, ipadx=20)
        self.volume_down.grid(row=6, column=1,  pady=10, ipady=20, ipadx=20)
        self.mute.grid(row=7, columnspan=2,  pady=10, ipady=20, ipadx=20)

        self.back.grid(row=8, columnspan=2,  pady=10, ipady=20, ipadx=20)

        self.frame.pack(expand=True)






#root = tk.Tk()
#app = Gui(root, my_device)
#root.mainloop()
