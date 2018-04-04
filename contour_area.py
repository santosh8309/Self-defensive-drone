import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (9, 9), 2)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([70, 85, 0])
    upper_blue = np.array([125, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
         area = cv2.contourArea(contour)
         if area > 5000:
             cv2.putText(img=frame, text='Warning', org= (155,180),
                         fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=2,
                         color=(0, 0, 255))
    cv2.drawContours(frame,contours,-1, (0,255,0),2)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()