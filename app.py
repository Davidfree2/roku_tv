import tkinter as tk
from plugins.roku import Roku

my_device = Roku("192.168.1.64", "8060")

window = tk.Tk()

window.title("Roku Remote")

frame = tk.Frame(window) 

left = tk.Button(frame, text='left', command=my_device.left)
right = tk.Button(frame, text='right',command=my_device.right)
up = tk.Button(frame, text='up', command=my_device.up)
down = tk.Button(frame, text='down', command=my_device.down)
home = tk.Button(frame, text='home', command=my_device.roku_home)
rev = tk.Button(frame, text='reverse', command=my_device.reverse)
forward = tk.Button(frame, text='forward', command=my_device.fast_forward)
select = tk.Button(frame, text='select', command=my_device.select)

up.grid(row=0, columnspan=2, pady=10, ipady=20, ipadx=20)
left.grid(row=1)
right.grid(row=1, column=1)
down.grid(row=2, columnspan=2, pady=10)
home.grid(row=4, columnspan=2, pady=10)
rev.grid(row=3, column=0, pady=15)
forward.grid(row=3, column=1)
select.grid(row=5, columnspan=2, pady=10)

frame.pack(expand=True)

window.mainloop()
