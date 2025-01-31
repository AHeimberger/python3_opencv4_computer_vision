# Custom Object Detectors

Algorithms that have a good ability to generalize or extrapolate, in the
sense that they can cope with the real-world diversity that exists within
a given class of object (cars different designs, people different shapes,
...).

- Histogram of Oriented Gradients (HOG)
- Non-Maximum Suppression (NMS) aka Non-Maxima Suprression
- Support Vector Machines (SVMs)
- Bag-of-Words (BoW)


## HOG Descriptors

HOG (Histogram of Oriented Gradients) is an image descriptor like SIFT,
SURF, and ORB, used for feature matching, object detection, and recognition.

It works by dividing an image into cells, computing gradient orientations
in each cell, and forming histograms. The number of bins corresponds to the
number of gradient directions. Cells are then grouped into blocks,
typically 2×2, for normalization.

To handle variations in object location and scale, a fixed-size sliding
window scans the image, and an image pyramid is used for multi-scale
detection. Overlapping detections are resolved using Non-Maximum Suppression
(NMS), ensuring only the highest-confidence detection is retained.

- https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf
- https://learnopencv.com/histogram-of-oriented-gradients/
- https://people.csail.mit.edu/torralba/publications/ihog_iccv.pdf
- https://www.cs.columbia.edu/~vondrick/ihog/


## NMS

- Construct image pyramid
- Scan each level of the pyramid with the sliding window approach
- Sort the list of positive detections, best first
- For each window "W" in the list of positive detections, remove all
  subsequent windows that significantly overlap with "W". We are left
  with a list of positive detections.

To determine the confidence score for a window, we need a classification
system that determines, whether a certain feature is present or not and
a confidence score for this classification. There we need SVMs.


## SVMs

It is a discriminative classifier formally defined by a separating hyperplane.
In other words, given labeled training data (supervised learning), the
algorithm outputs an optimal hyperplane which categorizes new examples.

- https://docs.opencv.org/3.4/d1/d73/tutorial_introduction_to_svm.html
- https://link.springer.com/content/pdf/10.1007/BF00994018.pdf

## BoW

Sometimes called: Bag of **visual** Words. Originally Bow belongs to the
field of language analysis and information retrieval. Technique by which
we assign a weight or count to each word in a series of documents and
then represent these documents with vectors of these counts. That allows
us to build up a dictionary, aka codebook.

Example:

Documents:
- Document 1: I like OpenCV and I like Python
- Document 2: I like C++ and Python
- Document 3: I dont like Artichokes

Dictionaries:
{
  I: 4,
  like: 4,
  OpenCV: 1,
  C++: 1,
  and: 2,
  Python: 2,
  dont: 1,
  Arthichokes: 1
}

Matrix:
[
  [I, like, OpenCV, C++, and, Python, dont, Arthichokes]
  [2, 2, 1, 0, 1, 1, 0, 0] cnt in Document 1
  [1, 1, 0, 1, 1, 1, 0, 0] cnt in Document 2
  [1, 1, 0, 0, 0, 0, 1, 1] cnt in Document 3
]

Vectors can be conceptualized as histogram representation fo documents
or as a decriptor vector that can be used to train claissifieres.

Applying:
- Take a sample dataset of images
- For each image in the dataset, extract descriptors
- Add each descriptor vector to the BoW trainer
- Cluster the descriptors into k clusters whose centers are our visual words


## K-Means Clustering

Method of quantization. We analyze a number of vectors in order to find a small
number of clusters.

- https://docs.opencv.org/4.x/de/d4d/tutorial_py_kmeans_understanding.html


## Detecting Cars

- Train Classifier: Images with cars (positive samples) and without cars (negative samples)
- Already available Datasets: UIUC Image Database for Car Detection and Stanford Cars Dataset
