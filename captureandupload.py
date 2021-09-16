import cv2

def takesnapshot():
    #initializing cv to module
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while (result):
        #read the frames whle camera is on
        ret, frame = videocaptureobject.read()
        cv2.imwrite("newpicture2.jpg", frame)
        result = False
    videocaptureobject.release()
    cv2.destroyAllWindows

takesnapshot()
