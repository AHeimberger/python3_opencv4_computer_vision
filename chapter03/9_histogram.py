import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('../images/kennedy_space_center.jpg')

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])
    plt.subplot(1, 2, 2)
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()
