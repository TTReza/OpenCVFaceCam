#laptop er webcam on korbo
import cv2 as cv
cam = cv.VideoCapture(0) #0 hocche default cam.

while cam.isOpened():
    ret, frame = cam.read() #amar webcam retrive kore frame e
    #ana holo
    if cv.waitKey(6) == ord('c'): #c chaple cam off hobe
        break
    cv.imshow("My cam", frame)
    #run kori asho


