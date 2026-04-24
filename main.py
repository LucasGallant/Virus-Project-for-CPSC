import you_exe as you
import desktopChange as dc
import time
from pathlib import Path


# On startup
you.startUp()

# wait until mood > 2
while True:
    time.sleep(.5)
    if you.get_mood() >= 3:
        # Use functions defined in desktopChange.py here, with respect to order and timing
        if (Path("_image.png").is_file()):
            dc.set_wallpaper("_image.png")
        else:
            dc.set_wallpaper("default.png")
        for i in range(100):
            time.sleep(1)
            dc.changeIcons()
        break
