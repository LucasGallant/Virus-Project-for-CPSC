import cv2, os, sys, keyboard, threading
from tkinter import *
from pathlib import Path
import tkinter as tk

def initialize():
    os.chdir(Path(__file__).parent)
    print(Path(__file__).parent)
    pass

def startUp():
    initialize()
    t1 = threading.Thread(target=display_image_unclosable)
    t2 = threading.Thread(target=always_on)
    # Take picture of the user
    take_picture()
    t1.start()
    t2.start()


def always_on():
    while True:
        if(keyboard.is_pressed('p')):
            os._exit(0)


def take_picture():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No more cap")
            break
        cv2.imwrite(filename="_image.png", img=frame)
        cv2.destroyAllWindows()
        break

    cap.release()


def display_image_unclosable():
    while True:
        root = Tk()
        root.geometry("500x400")
        photo = PhotoImage(file="_image.png", height=500, width=500)
        label = Label(root, image = photo)
        label.pack()
        if keyboard.is_pressed('p'):
            print("Key pressed!")
        root.mainloop()

