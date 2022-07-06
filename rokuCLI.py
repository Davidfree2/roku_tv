import sys
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

    def back(self):
        print("executing-------")
        try:
            roku_command = f'''curl -d '' "http://{self.ip_address}:{self.port}/keypress/Back"'''
            os.system(roku_command)
            print('success!')
        except:
            print("failed. Is the ip address and port correct? is curl installed on machine?")


def cli_args():
    try:
        #make sure to change this depending on your device
        my_device = Roku("192.168.1.64", "8060")

        foo = {
                'home' : my_device.roku_home,
                'mute' : my_device.roku_mute_unmute,
                'off' : my_device.roku_power_off,
                'forward' : my_device.fast_forward,
                'reverse' : my_device.reverse,
                'select' : my_device.select,
                'left' : my_device.left,
                'right' : my_device.right,
                'up' : my_device.up,
                'down' : my_device.down,
                'info' : my_device.info,
                'vol-down' : my_device.roku_volume_down,
                'vol-up' : my_device.roku_volume_up,
                'back' : my_device.back,
            }


        foo[str(sys.argv[1])]()

    except:
        print('''
Oops! It looks like you either didnt type in a command or used a wrong one.

These are the current avalible commands <home, mute, off, forward, reverse, select, left, right, up, down, info, vol-down, vol-up, back > 

EXAMPLE <python3 cli.py home> <python3 cli.py off> <python3 cli.py vol-down>

EXAMPLE WITH EXECUTABLE IN ~/.local/bin/ with chmod +x <rokucli home> <rokucli off> <rokucli vol-down>

If this is still not working try messaging me on github or leaving an error comment
        ''')


if __name__ == '__main__':
    cli_args()










