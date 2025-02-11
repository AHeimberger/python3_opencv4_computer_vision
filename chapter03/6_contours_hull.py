import cv2
import numpy as np

OPENCV_MAJOR_VERSION = int(cv2.__version__.split('.')[0])

img = cv2.pyrDown(cv2.imread("../images/hammer.jpg"))

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

black = np.zeros_like(img)
for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    hull = cv2.convexHull(cnt)
    cv2.drawContours(black, [cnt], -1, red, 2)
    cv2.drawContours(black, [approx], -1, green, 2)         # approximated hull
    cv2.drawContours(black, [hull], -1, blue, 2)            # convex hull

cv2.imshow("hull", black)
cv2.waitKey()
cv2.destroyAllWindows()
