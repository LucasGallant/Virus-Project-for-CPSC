import ctypes as ct
import os
def attackStart():
    print("hello world!")

def attack_name():
    pass

def set_wallpaper(path):
    absolute_path = os.path.abspath(path)
    ct.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)
