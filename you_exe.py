import cv2, os, sys, keyboard, threading, random
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
    #take_picture()
    t1.start()
    t2.start()

def always_on():
    while True:
        if(keyboard.is_pressed('p')):
            os._exit(0)

        # we are going to have to use a seperate thread for this or else our keybind will never be listened too.
        if(mood == 0):
            prompt_popups(0)
        if(mood == 1):
            prompt_popups(1)
        if(mood == 2):
            prompt_popups(2)
        else:
            prompt_popups(3)


        
    


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
    global mood
    mood = 0
    while True:
        root = Tk()
        root.geometry("500x400")
        photo = PhotoImage(file="_image.png", height=500, width=500)
        label = Label(root, image = photo)
        label.pack()
        #prompt_popups()
        root.mainloop()

def prompt_popups(indicator):

    friendly_prompts = ["Hello I am you.exe!", "I am you!", "Good day!", "Hello there"]
    agitated_prompts = ["Thats not very nice", "I thought we were friends", "Why would you do that?", "I am not happy with you"]
    Angry_prompts = ["I am very angry with you", "How could you do that?", "You were my friend."]
    Meltdown_prompts = ["Total destruction", "Your PC is mine", "I control you", "I am you"]

    if indicator == 0:

        top = Toplevel()
        top.geometry("500x400")
        label = Label(top, text=random.choice(friendly_prompts))
        label.pack()
        top.mainloop()
    if indicator == 2:
        pass
    if indicator == 3:
        pass
    else:
        pass


