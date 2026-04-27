import you_exe as you
import desktopChange as dc
import imageAlteration as ia
import time
from pathlib import Path



# On startup
you.startUp()

# wait until mood > 2
while True:
    time.sleep(.5)
    if you.get_mood() == 2:
        # Use functions defined in desktopChange.py here, with respect to order and timing
        if (Path("_image.png").is_file()):
            ia.contrast("_image.png")
            ia.invertColors("_image.png")
            #dc.set_wallpaper("_image.png")
        else:
            ia.contrast("default.png")
            ia.invertColors("default.png")
            #dc.set_wallpaper("default.png")
    if you.get_mood() == 3:
        if (Path("_image.png").is_file()):
            dc.set_wallpaper("_image.png")
        else:
            dc.set_wallpaper("default.png")
        for i in range(100):
            time.sleep(.25)
            dc.changeIcons()
        break