import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt
image = cv.imread('D:/YOMTECH PROJECTS/my python/test/hand1.png')

#image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
if image is None:
    sys.exit("not image")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# Define the color range for red
lower_red = np.array([0, 0, 100], dtype=np.uint8)
upper_red = np.array([100, 100, 255], dtype=np.uint8)

# Create a mask
mask = cv.inRange(image, lower_red, upper_red)

k = np.ones((2,2), np.uint8)

close = cv.morphologyEx(mask, cv.MORPH_OPEN, k)

contours, __ = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

font = cv.FONT_HERSHEY_SIMPLEX
count = 1
uplist = []

for contour in contours:
    (x, y), radius = cv.minEnclosingCircle(contour)
    coor  = (int(x),int(y))
    radius = int(radius)
    count1 = "No = %s, X = %s"%(count,coor[0])
    if radius > 30 or coor[1] < 150 or coor[0] >= 500:
        if radius > 30:
            continue
        cv.putText(image, count1, coor, font, 0.4, (0,0,255), 1)
        cv.circle(image, coor, radius, (0,255,0), 3)
        uplist.append(coor)
        continue
    cv.circle(image, coor, radius, (0,255,0), 3)
   
    cv.line(image,coor,(310,380), 255, 10)
    cv.circle(image, (310,380), 50, (0,255,0), -1)
    cv.putText(image, count1, coor, font, 0.4, (0,0,255), 1)
    if count == 1:
        shape = image.shape
        x,y,__ = shape
        if coor[0] <= x/2:
            cv.putText(image, "Right hand", (240,580), font, 1.1, 255,4)
        else:
            cv.putText(image, "Left hand", (240,580), font, 1.1, 255,4)
    count += 1
    
    

#plt.imshow(image, cmap="gray")
#plt.show()
cv.imshow("image", image)

cv.waitKey(0)
