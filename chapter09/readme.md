# Camera Models and Augumented Reality

Relationship between 3D Space and 2D Projection. Technical challenges:

- Modeling the parameters of a camera and lens
- Modeling a 3D object using 2D and 3D keypoints
- Detecting the object by matching keypoints
- Finding the objects 3D pose
- Smoothing the 3D pose using a Kalman filter
- Drawing graphics atop the object


## 3D Image Tracking and Augmentd Reality

3D Tracking is the process of continually updating an estimate of an objects
pose in a 3D space. Typically in terms of six variables, three variables to
represent the objects translation (that is position), other three variables
to represent its 3D rotation.

Other Term: **6DOF Tracking**

Representing the 3D Rotation of variables:
- Euler Angle Representation (3 separate 2 rotations around x, y, z)
- Rodrigues rotation vector
    - t_x - translation along x axis
    - t_y - translation along y axis
    - t_z - translation along z axis
    - r_x - first element of the objects rotation vector
    - r_y - second element of the objects rotation vector
    - r_z - third element of the objects rotation vector
    - Vector r_x, r_y, r_z encodes an axis of rotation and an angle of
      rotation about this axis

The camera is the origin of the 3D coordinate system, therefore the cameras
current t and r vectors are all defined to be 0, in any given frame. Other
objects are tracked relatively to the camera.


## Augmented Reality

Process of continually tracking relationships between real-world objects
and applying these relationships to virtual objects. In such a way that a
user preceives the virtual objects as beeing anchored to something in the
real world.

Steps involved in 3D Image Tracking and visual AR:
- Define parameters of the camera and lens
- Initialize a Kalman filter that will be used to stabilize the 6DOF tracking result
- Choose a reference image, representing the surface of the object
- Create a list of 3D points, representing the vertices of the object
- Extract feature descriptors from the reference image
- Convert the feature descriptors from pixel coordinates to 3D coordinates
- Start capturing frames from the camera
  - Extract feature descriptors, and attempt to find good matches between the
    reference image and the frame
  - If an insufficient number of good matches were found, continue to the next frame.
    Otherwise, proceed with the remaining steps
  - Attempt to find a good estimate of the tracked objects 6DOF pose based on the
    camera and lens parameters
  - Apply the Kalman filter to stabilize the 6DOF pose
  - Based on camera and lens parameters and 6DOF tracking results, draw a projection
    of some 3D graphics atop the tracked object in the frame


## Camera and Lens Parameters

- subject - the thing we want to capture
- lens - which transmits light and focuses any reflected light from the focal plane onto the image plane
  - optical center - point wher incoming light from the focal plane converges before being projected back
  - focal distance - distance between the optical center and the image plane
  - focal length - distance between optical center and the image plance, when focal distance is infinite
  - image sensor - photosensitive surface that receives light and records it
  - field of view - trigonometric relationship to the focal length, image sensord width and height

TODO: picture explains it really well


## Self Learning

- Image 1: Detect ArUco Marker
- Get Dimension of ArUco Marker
- Image 2: Perform Perspective Transformation
- Image 1: Remove ArUco Marker using Inverse Mask
- Image 1 + Image 2: Combine Images (BitwiseAnd)

- https://en.wikipedia.org/wiki/ARTag
- https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html
- https://medium.com/@gausic10/creating-augmented-reality-experiences-with-opencv-a-step-by-step-guide-63f9b757707f
- https://chev.me/arucogen/
- https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/Projet+calibration-Paul.html