# Tracking Objects

Detect objects based on differences between the current frame and a frame
that represents the background.

Background Subtraction
- Mixture of Gaussians (MOG)
- k-nearest neighbors (KNN)
- Godbehere-Matsukawa-Goldberg (GMG)

Track Moving Objects : Based on a color histogram, involves histogram back-projection
- MeanShift
- CamShift

Find a Trend in an Object
- Kalman-Filter


## Basic Background Substractor

- Suppose stationary camera that makes a reference image (background)
- Suppose something moves through the pictures
- Subtract background from moved picture


## MOG Background Subtractor

- Foreground segments marked white
- Background segments marked black
- Shadow segments marked gray
- GrabCut updates the foreground/background model over time


## GMG Background Subtractor

- opencv implementation of GMG does not differentiate between shadows
  and solid objects, so the detection rectancgles are elongated


## Background Subtractor Limitations

- change in exposure, change in lightning conditions can
  cause a change in pixel values, therefore the background image becomes
  invalid over time and needs to be updated
- shadows can affect the background
- objects that did not move in the picture for a long time
- lucerne lightning of the lamp caused many changes in picture


## Robust Tracking System

Important to build some kind of model of foreground objects rather than just the background
Color histogram has some properties that are particulary appealing in the context of
moition tracking. Histogram serves as a lookup table that directly maps pixel values to
probabilities. Perform tracking with very fine spatial resolution in real time.


## MeanShift

Performs tracking iteratively by computing a centroid based on probability.
Values in the current tracking recangle, shifting the rectangles center to this centroid,
recomputing the centroid based on values in the new rectangle, shifting the rectangle again,
and so on. Process continues until convergence is achieved or until a maximum number of
iterations is reached. MeanShift is a clustering algorithm.


## Kalman Filter

Developed already in 1950 by Rudolf Kalmann, found practical applications in many fields.
Operatores Recursively on a stream of noisy input data to produce a statistically optimal
estimate of the underlying system state. In the context of computer vision it can smoothen
the estimate of a tracked objects position.

Precict and Update Phase
- **Predict**: First phase: The filter uses the covariance calculated up to the current point
  in time to estimate the objects new position
- **Update**: Second phase: The filter records the objects position and adjusts the covariance
  for the next cycle of calculations. In OpenCV's terms this is called a **correction**.



## Lukas-Kanade Algorithm

- https://en.wikipedia.org/wiki/Lucas%E2%80%93Kanade_method
- https://www.youtube.com/watch?v=79Ty2Kkivvc&ab_channel=Jia-BinHuang
- https://docs.opencv.org/4.x/db/d7f/tutorial_js_lucas_kanade.html

