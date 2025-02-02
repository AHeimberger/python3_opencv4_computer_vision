import cv2
import os
import numpy as np

green = (0, 255, 0)
red = (0, 0, 255)

# Create a black image.
img = np.zeros((800, 800, 3), np.uint8)

# Initialize the Kalman filter.
# Based on the initialization, the kalman filter will track a 2D objects
# position and velocity. 
number_variables_tracked = 4 # x pos, y pos, x velocity, y velocity
number_variables_measured = 2 # x pos, y pos
kalman = cv2.KalmanFilter(number_variables_tracked, number_variables_measured)
# matrices describe the relationship between number_variables_tracked and measured
kalman.measurementMatrix = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0]], np.float32)
kalman.transitionMatrix = np.array(
    [[1, 0, 1, 0],
     [0, 1, 0, 1],
     [0, 0, 1, 0],
     [0, 0, 0, 1]], np.float32)
kalman.processNoiseCov = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]], np.float32) * 0.03

last_measurement = None
last_prediction = None

def on_mouse_moved(event, x, y, flags, param):
    global img, kalman, last_measurement, last_prediction

    measurement = np.array([[x], [y]], np.float32)
    if last_measurement is None:
        # This is the first measurement.
        # Update the Kalman filter's state to match the measurement.
        kalman.statePre = np.array([[x], [y], [0], [0]], np.float32)
        kalman.statePost = np.array([[x], [y], [0], [0]], np.float32)
        prediction = measurement
    else:
        kalman.correct(measurement)
        prediction = kalman.predict()  # Gets a reference, not a copy

        # Trace the path of the measurement in green.
        cv2.line(img, (int(last_measurement[0]), int(last_measurement[1])),
                 (int(measurement[0]), int(measurement[1])), green)

        # Trace the path of the prediction in red.
        cv2.line(img, (int(last_prediction[0]), int(last_prediction[1])),
                 (int(prediction[0]), int(prediction[1])), red)

    last_prediction = prediction.copy()
    last_measurement = measurement

cv2.namedWindow('kalman_tracker')
cv2.setMouseCallback('kalman_tracker', on_mouse_moved)

while True:
    cv2.imshow('kalman_tracker', img)
    k = cv2.waitKey(1)
    if k == 27:  # Escape
        if not os.path.exists("output"):
            os.mkdir("output")

        cv2.imwrite('./output/kalman.png', img)
        break
