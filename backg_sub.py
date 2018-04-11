import cv2
import numpy as np

cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    _, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    blurred_frame = cv2.GaussianBlur(fgmask, (3, 3), 3)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    _, contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(contours)
    for contour in contours:
         area = cv2.contourArea(contour)
         if area in range (3000,8000):
             cv2.putText(img=frame, text='Warning', org= (155,180),
                         fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=2,
                         color=(0, 0, 255))
    cv2.drawContours(frame,contours,-1, (0,255,0),2)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", fgmask)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()