import cv2, os, sys, keyboard, threading
from tkinter import *
from pathlib import Path
import tkinter as tk

# So i figured out the keybind press failing to end the program, it does work now, but you basically have to hold it while you are closing thje image.
# This is because the mainloop is the current running process and we can only do one thign at a time. 
# Edit: I implemented 2 threads, one that runs the always_on function which waits for key press,
# and one that runs the window where we must likely will put all are future functions in, or run more threads.


def setup():
    os.chdir(Path(__file__).parent)
    print(Path(__file__).parent)
    pass

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

# For now we will disable the attack method and this can be used to annoy later on in the program.
def attack():
    image1 = PhotoImage(file="_image.png")
    for i in range(5):
        top = Toplevel()
        label = Label(top, image=image1)
        label.pack()
    top.mainloop()

def display_image_unclosable():
    while True:
        root = Tk()
        root.geometry("500x400")
        photo = PhotoImage(file="_image.png")
        label = Label(root, image = photo)
        label.pack()
        if keyboard.is_pressed('p'):
            print("Key pressed!")
        root.mainloop()
        

    
    

def main():
    setup()
    t1 = threading.Thread(target=display_image_unclosable)
    t2 = threading.Thread(target=always_on)
    t1.start()
    t2.start()

    #root = Tk()
    #take_picture()
    #button = Button(root, text="Press me to attack", command=attack(), font=(20))
    ##button.pack()
    #root.mainloop()

main()

