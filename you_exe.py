from tkinter import *
from pathlib import Path
import tkinter as tk
import cv2, os

# test
# I disabled the attack method so now it just takes the picture and stores it in the root folder.
# We Will use the picture for our other functions, and it is stored as _image.png

def setup():
    os.chdir(Path(__file__).parent)
    print(Path(__file__).parent)
    pass


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

def display_image():
    print("h")
    root = Tk()
    yourPhoto = PhotoImage(file="_image.png")
    label = Label(root, image=yourPhoto).pack()
    root.mainloop()
    

def main():
    setup()
    #root = Tk()
    #take_picture()
    #button = Button(root, text="Press me to attack", command=attack(), font=(20))
    ##button.pack()
    #root.mainloop()

main()
display_image()
