import cv2 as cv

def readAndShowImage(path, resize=None, func=None):
    image = cv.imread(path)

    if resize:
        image = resize(image)

    if func:
        image = func(image)
    
    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def readAndShowVideo(path, resize=None, func=None):
    cap = cv.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            if resize:
                frame = resize(frame)
            if func:
                frame = func(frame)
            
            cv.imshow('Video', frame)
   
        # Press Q on keyboard to exit
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    cv.waitKey(0)
    cv.destroyAllWindows()
