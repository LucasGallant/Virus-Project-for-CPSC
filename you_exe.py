import cv2, os, sys, keyboard, threading, random, time
from tkinter import *
from pathlib import Path
import tkinter as tk


def initialize():
    os.chdir(Path(__file__).parent)
    print(Path(__file__).parent)
    pass


def thread_handling():
    t1 = threading.Thread(target=display_image_unclosable)
    t2 = threading.Thread(target=always_on)

    # Take picture of the user
    #take_picture()

    t2.start()
    time.sleep(.1)
    t1.start()

def startUp():
    initialize()
    thread_handling()


def always_on():
    while True:
        if(keyboard.is_pressed('p')):
            os._exit(0)


# Ran as a seperate thread from the display_image_unclosable func
def prompt_popup_status_running():
    time.sleep(1)
    prompt_popups(mood)
    



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


# Displays an image that cannot be closed and also starts a thread that prompts popups when ran, and window is closed
def display_image_unclosable():
    global mood
    mood = 0
    while True:
    
        t_ = threading.Thread(target=prompt_popup_status_running)

        top = Tk()
        top.geometry("500x400")
        photo = PhotoImage(file="_image.png", height=500, width=500)
        label = Label(top, image = photo)
        label.pack()
        t_.start()
        print(mood)
        top.mainloop()
        mood+=1
        
# handles all the display of the prompts based on mood
def prompt_popups(indicator):

    friendly_prompts = ["Hello I am you.exe!", "I am you!", "Good day!", "Hello there"]
    agitated_prompts = ["Thats not very nice", "I thought we were friends", "Why would you do that?", "I am not happy with you"]
    Angry_prompts = ["I am very angry with you", "How could you do that?", "You were my friend."]
    Meltdown_prompts = ["Total destruction", "Your PC is mine", "I control you", "I am you"]

    time.sleep(.1)
    try:
        top = Toplevel()
        if indicator == 0:
            msg = random.choice(friendly_prompts)
        elif indicator == 1:
            msg = random.choice(Angry_prompts)
        elif indicator == 2:
            msg = random.choice(agitated_prompts)
        elif indicator >= 3:
            msg = random.choice(Meltdown_prompts)
        else:
            msg = "something went wrong"
        
        label = Label(top, text=msg)
        top.geometry("200x100+650+250")
        label.pack()

    except Exception as e:
        print(e)



