#!/usr/bin/python3

import tkinter as tk
from plugins.roku import Roku
from plugins.gui import Gui




def main():

    device_ip =  ''.join(open('./device_info/device_ip.txt', 'r').read().splitlines())
    device_port = ''.join(open('./device_info/device_port.txt', 'r').read().splitlines())
    #change device based on your ip address and port number
    my_device = Roku(str(device_ip), str(device_port))

    root = tk.Tk()
    app = Gui(root, my_device)
    root.mainloop()




main()
