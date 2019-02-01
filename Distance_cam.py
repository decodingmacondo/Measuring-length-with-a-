from scipy.spatial import distance as dist
import numpy as np
import cv2
 
drawing = False
point1 = ()
point2 = ()
d=[]
 
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5) 

def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
        else:
            drawing = False
            dA = dist.euclidean((int(point1[0]), int(point1[1])), (int(point2[0]), int(point2[1])))
            d.append(dA)
            print(d)
 
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x, y)
 
 
cap = cv2.VideoCapture(0)
 
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)
 
 
while True:
    _, frame = cap.read()
 
    if point1 and point2:
        cv2.line(frame, point1, point2, (0, 255, 0))
        dA = dist.euclidean((int(point1[0]), int(point1[1])), (int(point2[0]), int(point2[1])))
        (tltrX, tltrY) = midpoint(point1, point2)
        cv2.putText(frame, "{:.1f}px".format(dA),(int(tltrX - 25), int(tltrY - 20)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 1)
 
    cv2.imshow("Frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
 
cap.release()
cv2.destroyAllWindows()