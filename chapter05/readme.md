# Detecting and Recognizing Faces

- face detection - locating faces in an images
- face recognition - identifying a face as a specific person


## Haar Cascade Classifier

- https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d
- https://www.analyticsvidhya.com/blog/2022/10/face-detection-using-haar-cascade-using-python/


## Face Recognition Algorithms

- Eigenfaces
- Fisherfaces
- Local binary Pattern Histograms (LBPHs)


## Conceputualizing Haar Cascades

- some means of abstracting image detail is useful in producing stable classification and tracking results
- features - abstractions are called features, which are extracted from the image data
    - fewer features than pixels :) - set of features represented as a vector
    - haar-like features have been first used from "Paul Viola" and "Michael Jones"
    - edges, vertices, and thin lines each generate a kind of feature
- cascade - features can be organized into a hierarchy
    - highest - contain features of greatest distinctiveness
- window size - features may vary depending on the scale of the image and the size of the neighborhood 
- scale invariance - to make it robust to changes in scale (window size is constant, but image resized)
- image pyramid - original image and the rescaled images together


## Haar Cascade Data

- saved on opencv https://github.com/opencv/opencv/tree/master/data/haarcascades
  provided by Joseph Howes
- frontal, upright view of the subject
- learn how to train a cascade: opencv4 for secret agents, chapter 03


## Databases

- http://www.face-rec.org/databases
- Yale Face Database (Yalefaces)
- Extended Yale Face Database B
- Database of Faces (from AT&T Laboratories Cambridge)


## Algorithms to Recognize Faces

- Principal Component Analysis (PCA) - https://arxiv.org/pdf/1404.1100v1, https://pca.narod.ru/pearson1901.pdf
  - Eigenfaces - https://sites.cs.ucsb.edu/~mturk/Papers/jcn.pdf
  - Fisherfaces - https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x
- Local Binary Pattern Histograms (LBPHs) - https://ieeexplore.ieee.org/document/576366


## Algorithms Approach

1. take a set of classified observations
2. train a model based of those observations
3. perform an analysis of the images
4. determine two things
  - the subjects identity
  - a measure of confidence - Confidence Score


## Confidence Scorces

- Eigenface, Fisherface - values in the range of 0 to 20000
  - scores below 4000,5000 being quite confident
- LBPH good recognition below 50 and above 80 considered poor


## Detection in the Night

- Near Infrared Camera (NIR)