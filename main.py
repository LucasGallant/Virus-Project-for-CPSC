import you_exe as you
import desktopChange as dc
import time


# On startup
you.startUp()

# wait until mood > 2
while True:
    time.sleep(.5)
    print(you.get_mood())
    if you.get_mood() >= 3:
        # Use functions defined in desktopChange.py here, with respect to order and timing

        break

print("pen test complete!")

#dc.set_wallpaper("funny.png")
