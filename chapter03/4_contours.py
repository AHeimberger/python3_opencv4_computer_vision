import cv2
import numpy as np

OPENCV_MAJOR_VERSION = int(cv2.__version__.split('.')[0])

# Create a black image.
img = np.zeros((300, 300), dtype=np.uint8)

# Draw a square in two shades of gray.
img[50:150, 50:150] = 160
img[70:150, 70:150] = 128

# Apply a threshold so that the square becomes uniformly white.
ret, thresh = cv2.threshold(img, 127, 255, 0)

# Find the contour of the thresholded square.
# - cv2.RETR_TREE - retrieve the entire hierarchy of external and internal contours
# - cv2.RETR_EXTERNAL - retrieve the most external contours (use when object appears on a plain background)
contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
