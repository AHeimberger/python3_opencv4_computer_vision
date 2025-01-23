import cv2
import numpy as np

img = cv2.imread("../images/nasa_logo.png")
cv2.imshow("my image", img)
print("press any key to close")
cv2.waitKey()
cv2.destroyAllWindows()
