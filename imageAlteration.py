import cv2

def invertColors(imgName):
    img = cv2.imread(imgName)
    inverseImage = 255 - img
    cv2.imwrite(imgName, inverseImage)

def sharpen(imgName, runNum):
    for i in range(runNum):
        sharpenedImage = cv2.Laplacian(imgName, cv2.CV_64F)
        cv2.imwrite(imgName, sharpenedImage)