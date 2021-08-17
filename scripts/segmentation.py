import cv2 as cv

from .utils import resize

def applyCannyEdgeDetection(image, minVal=25, maxVal=60):
    # Convert image to gray scale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Apply canny edge detection
    edges = cv.Canny(gray, minVal, maxVal)

    return edges

def applyFloodFill(image, mask):
    # Apply Threshold
    ret,flooded = cv.threshold(image, 5, 5, cv.THRESH_BINARY)

    # Apply FloodFill
    cv.floodFill(flooded, mask, (0, 0), 255)

    return flooded

def applyDilation(image):
    image = cv.dilate(image, (3, 3), iterations=1)
    return image

def applySegmentation(image):
    edges = applyCannyEdgeDetection(image)
    resized_edges = resize(edges, 514, 514)
    
    flooded = applyFloodFill(image, resized_edges)
    
    flooded = cv.bitwise_not(flooded)
    image = cv.bitwise_and(image, flooded)

    dilatedImage = applyDilation(image)

    return dilatedImage