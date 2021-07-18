import numpy as np
import cv2 as cv
import requests

url = 'http://10.19.170.105:8080/shot.jpg'
while True:
    r = requests.get(url)
    img_arr = np.array(bytearray(r.content),dtype=np.uint8)
    img = cv.imdecode(img_arr, -1)
    cv.imshow('IPWebcam', img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()


