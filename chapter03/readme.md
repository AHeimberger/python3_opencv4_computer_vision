# Processing Images

## color models

- in computing be typically work with dree kinds of color models
    - grayscale - each pixel single 8-bit value (shades of grey or brightness)
    - blue-green-red (bgr) - each pixel a triplet of 8-bit value
    - hue-saturation-values (hsv) - hue is the colors tone, saturation is intensity, value is brightness
- models that deal with light are called additive models (computer emits light)
- models that deal with paint are called subtractive models


## exploring fourier

- waveforms ar just the sum of simple sinusoids of different frequencies
- waveforms ar the sum of other waveforms
- numpy fast-fourier-transform package
    - fft2 method allows to comput a discrete fourier transform dft

magnitude spectrum is a representation of the original image in terms of changes
- draging all bright pixels to the center
- draging all dark pixel to the border
- able to see number of light and dark pixels and the percentage of their distribution

fourier transform is used for 
- edge detection
- line and shape detection
- HPFs (High-Pass Filters)
- LPFs (Low-Pass Filters)
- ...

kernel is a set of weights applied to a region
- ksize of 7 = 7*7 (49 pixel)

another term for kernel is convolution matrix
- mixes up or convoles the pixels in a region

Kernel gives average differenc in intensity between
the central pixel and all its immedia horizontal neighbors.

```
[
    [0, -0.25, 0],
    [-0.25, 1, -0.25],
    [0, -0.25, 0]
]
```
- values in kernel sum up to 0

If the pixel stands out from the surrounding pixels,
the resulting value will be high. Kernel is a HPF, used for
edge detection.


## edge detection

edge-finding filters: laplacian, sobel, schwarr
    - turns non edge regions into black 
    - turns edge regions into white or saturated colors
blurring filters: blur (simple average), medianBlur, gaussianblur

when to choose which
- medianBlur effective in removing digital video noise especially color images
- laplacian produces bold edge especially in grayscale images

how to
1. convert bgr in grayscale
2. use medianBlur
3. use laplacian
4. invert image
4. normalize image (range from 0 to 1)
5. multiply image with source image to darken edges


## edge detection with canny

1. denoise the image using gaussian filter
2. calculate the gradients
3. apply non-maximum suppression (NMS) on the edges
    - algorithm selects the best edges from a set of overlapping edges
4. apply double treshold to all the edges (elimate false positive)
5. analyze and discard weak edges


## contour (object outlines) detection

- Kontur = äußere Linie eines Körpers [die sich von einem Hintergrund abhebt]
- calculate regions of interest (ROIs)

better approach with douglas-peucker algorithm
- subjects with diverse shapes, including convex
- code works on simple images
    - only a few objects
    - only a few colors
    - good separation of thresholds


# detecting lines, circles, and other shapes

- line/shape detection foundation a technique called hough transform (richard duda, peter hart)
    - extended work of paul hough
- opencv implementation of the hough transform limited to lines and circles
- approxPolyDP - allows approximation of polygons
    - if image contains polygons can be detected with findContours and approxPolyDP

