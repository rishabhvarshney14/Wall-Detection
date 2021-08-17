import cv2 as cv

def resize(image, width=512, height=512):
    image = cv.resize(image, (width, height))
    return image