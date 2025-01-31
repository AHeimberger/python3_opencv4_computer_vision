import cv2
import numpy

red = [0, 0, 255]
# by tweaking the block_size, smaller_regions for smaller values, or larger_regions
# for larger values will be detected as corners
block_size = 2
# the sobel operator detects edges by measuring horizontal and vertical differences,
# between pixel values in a neighboorhood and it does this by using a kernel.
# the size of the kernel defines how sensitive corner detection is
# parameter needs to be between 3 (high sensitive) and 32 (low sensitive)
kernzel_size = 23
k = 4

def update(sliderValue=0):
    try:
        block_size = cv2.getTrackbarPos('block_size', 'CornerHarris')
        kernel_size = cv2.getTrackbarPos('kernel_size', 'CornerHarris')
        k = cv2.getTrackbarPos('k', 'CornerHarris')
    except cv2.error:
        # One or more of the sliders has not been created yet.
        return
    
    def round_up_to_odd(f):
        ret = int(numpy.ceil(f / 2.) * 2 + 1)
        return ret if ret <= 31 else 31

    img = cv2.imread('../images/chess_board.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cornerHarris returns an image in floating points
    # high score indicates the pixel is likely to be a corner
    dst = cv2.cornerHarris(gray, block_size, round_up_to_odd(kernel_size), k*1.0/100.0)
    # pixels with low score are treated as non corners
    img[dst > (0.01 * dst.max())] = red
    cv2.imshow('CornerHarris', img)


cv2.namedWindow('CornerHarris')
cv2.createTrackbar('block_size', 'CornerHarris', block_size, 10, update)
cv2.createTrackbar('kernel_size', 'CornerHarris', kernzel_size, 31, update)
cv2.createTrackbar('k', 'CornerHarris', k, 100, update)

update()

cv2.waitKey()
