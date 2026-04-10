from tkinter import *
import tkinter as tk
import cv2

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
        cv2.imwrite()
        cv2.destroyAllWindows()
        break

    cap.release()

    
def attack():
    image1 = PhotoImage(file=r"C:\Users\zacal\OneDrive\Desktop\Compsci\captured_image.png")
    for i in range(5):
        top = Toplevel()
        label = Label(top, image=image1)
        label.pack()
    top.mainloop()

def main():
    root = Tk()
    #take_picture()
    button = Button(root, text="Press me to attack", command=attack(), font=(20))
    button.pack()
    root.mainloop()


main()
