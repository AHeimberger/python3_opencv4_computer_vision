import cv2
import os
import numpy as np
from cv2 import aruco
import math
import matplotlib.pyplot as plt

# http://stackoverflow.com/questions/70352659/cv2-warpperspective-produces-black-dotted-edges

def image_shower(title, image):
    cv2.namedWindow(title, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bg_image = cv2.imread("./inputs/background.jpg")
pikachu_image = cv2.imread("./inputs/pikachu.jpg")

bg_h, bg_w, bg_ch = bg_image.shape
pikachu_h, pikachu_w, pikachu_ch = pikachu_image.shape
poster_topleft = [0, 0]
poster_topright = [pikachu_w, 0]
poster_bottomright = [pikachu_w, pikachu_h]
poster_bottomleft = [0, pikachu_h]

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)
arucocorners, ids, Error = detector.detectMarkers(bg_image)

aruco_topleft = arucocorners[0][0][0]
aruco_topright = arucocorners[0][0][1]
aruco_bottomright = arucocorners[0][0][2]
aruco_bottomleft = arucocorners[0][0][3]

start_point = (int(aruco_topleft[0]), int(aruco_topleft[1]))
stop_point = (int(aruco_bottomright[0]), int(aruco_bottomright[1]))

bg_image = cv2.rectangle(bg_image, start_point, stop_point, (0, 255, 0), 20)

input_corners = np.float32([poster_topleft, poster_topright, poster_bottomright, poster_bottomleft])
output_corners = np.float32([aruco_topleft, aruco_topright, aruco_bottomright, aruco_bottomleft])

matrix = cv2.getPerspectiveTransform(input_corners, output_corners)
pikachu_transformed = cv2.warpPerspective(pikachu_image, matrix, (bg_w, bg_h))
# image_shower("transform_poster", pikachu_transformed)

mask = np.zeros(bg_image.shape[:2], dtype="uint8")
cv2.rectangle(mask, start_point, stop_point, 255, -1)
mask_inverted = cv2.bitwise_not(mask)
# image_shower("Mask", mask_inverted)

bg_image_vanished_aruco = cv2.bitwise_and(bg_image, bg_image, mask = mask_inverted)
# image_shower("Remove Aruco", bg_image_vanished_aruco)

dst = cv2.add(bg_image_vanished_aruco, pikachu_transformed)
image_shower("Combined Images", dst)
