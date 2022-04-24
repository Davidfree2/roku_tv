import os
import time
import tkinter as tk


class Roku:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def roku_home(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Home"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def roku_volume_up(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/VolumeUp"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def roku_volume_down(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/VolumeDown"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def roku_mute_unmute(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/VolumeMute"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def roku_power_off(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/PowerOff"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def fast_forward(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Fwd"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def reverse(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Rev"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def select(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Select"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def left(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Left"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def right(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Right"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def up(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Up"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def down(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Down"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def info(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Info"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def find_remote(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/FindRemote"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def hdmi1(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/InputHDMI1"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def hdmi2(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/InputHDMI2"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def hdmi3(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/InputHDMI3"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")

    def hdmi4(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/InputHDMI4"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")













my_device = Roku("192.168.1.64", "8060")

window = tk.Tk()

left = tk.Button(text='left', command=my_device.left())
right = tk.Button(text='right',command=my_device.right())
up = tk.Button(text='up', command=my_device.up())
down = tk.Button(text='down', command=my_device.down())
home = tk.Button(text='home', command=my_device.roku_home())

left.pack()
right.pack()
up.pack()
down.pack()
home.pack()

window.mainloop()
