import threading
import you_exe as you
import desktopChange as dc
import time


you.startUp()


while True:
    time.sleep(.5)
    print(you.get_mood())
    if you.get_mood() >= 3:
        dc.attackStart()
        break

print("pen test complete!")

#dc.set_wallpaper("funny.png")