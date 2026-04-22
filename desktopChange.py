import ctypes as ct
import os
import win32gui
import random
import pyautogui

LVM_GETITEMCOUNT = 0x1004
LVM_SETITEMPOSITION = 0x100F
width, height = pyautogui.size()

def set_wallpaper(path):
    absolute_path = os.path.abspath(path)
    ct.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)

def find_desktop_listview():
    progman = win32gui.FindWindow("Progman", None)
    shell = win32gui.FindWindowEx(progman, None, "SHELLDLL_DefView", None)
    if not shell:
        worker = win32gui.FindWindowEx(None, None, "WorkerW", None)
        shell = win32gui.FindWindowEx(worker, None, "SHELLDLL_DefView", None)
    listview = win32gui.FindWindowEx(shell, None, "SysListView32", "FolderView")
    return listview

def changeIcons():
    listview = find_desktop_listview()

    # Number of icons
    count = win32gui.SendMessage(listview, LVM_GETITEMCOUNT)
    
    for i in range(count):
        x = random.randint(0, width - 100)
        y = random.randint(0, height - 100)

        win32gui.SendMessage(listview, LVM_SETITEMPOSITION, i,(y << 16) | x)
