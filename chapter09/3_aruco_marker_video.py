import cv2
import os
import numpy as np
from cv2 import aruco
import math
import matplotlib.pyplot as plt

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow("MyWindow")
cv2.setMouseCallback("MyWindow", onMouse)

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    pikachu_image = cv2.imread("./inputs/pikachu.jpg")

    bg_h, bg_w, bg_ch = frame.shape
    pikachu_h, pikachu_w, pikachu_ch = pikachu_image.shape
    poster_topleft = [0, 0]
    poster_topright = [pikachu_w, 0]
    poster_bottomright = [pikachu_w, pikachu_h]
    poster_bottomleft = [0, pikachu_h]

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters =  cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    arucocorners, ids, Error = detector.detectMarkers(frame)

    if len(arucocorners) == 0:
        cv2.imshow("MyWindow", frame)
        success, frame = cameraCapture.read()
        continue

    aruco_topleft = arucocorners[0][0][0]
    aruco_topright = arucocorners[0][0][1]
    aruco_bottomright = arucocorners[0][0][2]
    aruco_bottomleft = arucocorners[0][0][3]

    pts = np.array([aruco_topleft, aruco_topright, aruco_bottomright, aruco_bottomleft], np.int32)
    pts = pts.reshape((-1,1,2))
    frame = cv2.polylines(frame, [pts], True, (0,255,0), 5)

    input_corners = np.float32([poster_topleft, poster_topright, poster_bottomright, poster_bottomleft])
    output_corners = np.float32([aruco_topleft, aruco_topright, aruco_bottomright, aruco_bottomleft])

    matrix = cv2.getPerspectiveTransform(input_corners, output_corners)
    pikachu_transformed = cv2.warpPerspective(pikachu_image, matrix, (bg_w, bg_h))

    mask = np.zeros(frame.shape[:2], dtype="uint8")
    cv2.fillPoly(mask, [pts], (255, 0, 0))
    mask_inverted = cv2.bitwise_not(mask)
    
    bg_image_vanished_aruco = cv2.bitwise_and(frame, frame, mask = mask_inverted)
    dst = cv2.add(bg_image_vanished_aruco, pikachu_transformed)

    cv2.imshow("MyWindow", dst)
    success, frame = cameraCapture.read()

cv2.destroyWindow("MyWindow")
cameraCapture.release()
