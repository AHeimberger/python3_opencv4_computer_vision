# Depth Estimation and Segmentation

- depth camera to identify foreground and background regions
- other techniques "stereo imaging", "structure from motion (SfM)"

Depth-Sensing Cameras
- Stereo vision - use of two cameras simultaneously
- Time of flight
    - Direct Time-of-Flight (dToF)
        - LiDAR
    - Indirect Time-of-Flight (iToF)
- Structured light - uses a laser/LED light source to project light patterns
  (mostly a striped one) onto the target object. Based on the distortions
  obtained, the distance to the object can be calculated

Cameras
- Microsoft Kinect
- Asus Xtion
- Occipital Structure

Resource:
- https://www.e-consystems.com/blog/camera/technology/what-are-depth-sensing-cameras-how-do-they-work/


## Depth Camera
Each channel might correspond to different kinds of data
- normal color image
- depth map - grayscale image where value represents the depth
- point cloud map - BGR imag where B is x, G is y and R is z achses
- disparity maps - grayscale image where each pixel is the stereo disparity of the surface
    - camera takes picture of the same scene, in two different positions
    - we wish to recover the depth at each pixel
    - nearby objects exhibit greter stereo disparity than far off objects
    - nearby object appear brighter in a disparity map
    - https://johnwlambert.github.io/stereo/
- valid depth mask
- infrared (IR) or near infrared (NIR)
- ...


## Epipolar Geometry
Traces imaginary lines from the camera to each object in the image, then does the
same on the second image, and calculates the distance to an object based on the intersection
of the lines corresponding to the same object.

- https://en.wikipedia.org/wiki/Epipolar_geometry


## Semi Global Block Matching (SGBM)
About gathering three-dimensional information from two-dimensional pictures

## GrabCut
Perfect for foreground/background segmentation
1. a rectangle including the subject of the picture is defined
2. area lying outside the rectangle is automatically defined as background
3. data contained in the background is used as a reference to distinct
   background ares from foreground areas within the defined rectangle
4. a gaussian micture model (GMM) models the foreground and background,
   and labels undefined pixels as probable background and probable foreground
5. each pixel in the image is virtually connected to the surrounding pixels
   through virtual edges, and each edge is assigned a probability of being
   foreground or background, based on how similar it is in color to the pixels
   surrounding it
6. each pixel is connected to either a foreground or background node
7. after connection to either terminal, the edges belonging to different terminals
   are cut, image is segmented into two part


## Watershed Algorithm
Called so because its conceptualization involves water
- areas with low density in an image as valleys
- areas with high density as peaks

Start by filling the valleys with water, to the point where until water from
different valleys are about to merge. To prevent merging of water you build
a barrier to keep them separated. Resulting barriers ar the image segmentations.

- https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html