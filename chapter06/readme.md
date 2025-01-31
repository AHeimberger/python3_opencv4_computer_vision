# Using Descriptors

For retrieving and searching images.

A **descriptor** is a representation or vector that contains characteristic information about an image feature.
These descriptors are extracted from **keypoints** or **features** of an image in order to compare or recognize
these characteristics later.

- Detecting Keypoints and Extracting Local Descriptors
    - Harris Corners - to detect corners
    - SIFT (Scale-Invariant Feature Transform) - to detect blobs
    - SURF (Speeded-Up Robust Features)  - to detect blobs
    - FAST (Features from Accelerated Segment Test) - to detect corners
    - BRIEF (Binary Robust Independent Elementary Features) - to detect blobs
    - [ORB (Oriented FAST and Rotated BRIEF)](https://github.com/eYSIP-2016/Object-Tracking-Camera/blob/master/Research%20papers%20referred(Object%20Tracking)/orb_final.pdf) - combination of blobs and corners, mixes the techniques of FAST and BRIEF
- Matching Keypoints 
    - Brute Force
    - FLANN Algorithm (Fast Library for Approximate Nearest Neighbors)
- Spatial Verification
    - Homography
- Filtering Bad Matches
    - KNN Algorithm (K-Neirest Neighbors)
- Finding Homography between two sets of matching keypoints
- Searching a set of images to determine the best match for a reference image

A feature is an area of interest in the image that is unique or easily recognizable. Features of an image might be:

- Edges → Boundaries between objects 
- Blobs → Distinct regions in an image
- Corners → Points where two edges meet
- Ridges → Long, thin structures like veins or fingerprints

## Corners

Corners are even detected when the image is rotated. However if we scale an image,
some parts lose or even gain of corner quality using the Harris Corner Algorithm.
An algorithm that works regardless of the scale of the image is SIFT. SIFT does
not detect the keypoints, this is done by a Difference of Gaussian (DoG) algorithm.

## Keypoint Anatomy

`print(dir(keypoints[0]))`

- pt = x,y coordinate of the point
- size = diameter of the feature
- angle = orientation of the feature (see the radial line)
- response = strength of the feature
- octace = layer of the image pyramid where the feature was found
- class_id = can be used to assign a custom identifier

## FAST

Analyzes circular neighborhoods of 16 pixels. Marks each pixel in a neighboarhood as
brighter or darker than a particular treshold, which is defined relative to the
center of the circle. It is a corner if it contains a number of contiguous pixels 
marked as brighter or darker.

- https://docs.opencv.org/3.4/df/d0c/tutorial_py_fast.html

## BRIEF

- https://docs.opencv.org/3.4/dc/d7d/tutorial_py_brief.html

## Brute Force

- https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html


