import numpy as np
import cv2
from matplotlib import pyplot as plt

original = cv2.imread('../images/statue_small.jpg')

number_iterations = 5

def update(sliderValue=0):
    try:
        number_iterations = cv2.getTrackbarPos('iterations', 'GrabCut')
    except cv2.error:
        return

    img = original.copy()
    mask = np.zeros(img.shape[:2], np.uint8)

    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    rect = (100, 1, 421, 378)
    cv2.grabCut(img, mask, rect, background_model, foreground_model, number_iterations, cv2.GC_INIT_WITH_RECT)
    # mask has changed to contain values between 0 and 3
    # 0 - background pixel
    # 1 - foreground pixel
    # 2 - probable background pixel
    # 3 - probable foreground pixel
    mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
    # convert value 0 and 2 into 0
    # convert value 1 and 3 into 1
    img = img*mask2[:,:,np.newaxis]

    # paint rectangle around ROI
    img = cv2.rectangle(img, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 1)

    cv2.imshow('GrabCut', img)

cv2.namedWindow('GrabCut', cv2.WINDOW_NORMAL)
cv2.createTrackbar('iterations', 'GrabCut', number_iterations, 100, update)

update()

cv2.waitKey()
