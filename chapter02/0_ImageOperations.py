import numpy
import cv2
import os

if not os.path.exists("output"):
    os.mkdir("output")

print("\n3x3 black image")
img = numpy.zeros((3, 3), dtype=numpy.uint8)
print(img)

print("\nconvert image into blue-green-red (bgr)")
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)

print("\ncheck the structure of an image (rows, columns, number of channels) type tuple")
print("- no channel means grayscale")
img = numpy.zeros((5, 3), dtype=numpy.uint8)
print(img.shape)
print("- three channels per pixel")
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img.shape)

print("\nread as png and write as jpg")
image = cv2.imread("../images/stacked1.png")
cv2.imwrite("output/image.jpg", image)
print("- imread has different modes (IMREAD_COLOR, IMREAD_GRAYSCALE, ...)")
print("- https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html")
gr_image = cv2.imread("../images/stacked1.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("output/image_grayscale.jpg", gr_image)

print("\naccess value within image")
print(image[0, 0, 0])
print(gr_image[0, 0])

print("\nconvert into byte array")
bgr_ByteArray = bytearray(image)
gr_ByteArray = bytearray(gr_image)
# print(byteArray)
gr_image = numpy.array(gr_ByteArray).reshape(gr_image.shape[0], gr_image.shape[1])
bgr_image = numpy.array(bgr_ByteArray).reshape(image.shape[0], image.shape[1], image.shape[2])

print("\nconvert random bytes into a grayscale image")
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite("output/random_gray.png", grayImage)
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite("output/random_color.png", bgrImage)

print("\nchange pixel in image to black")
img = cv2.imread("../images/stacked1.png")
img[0, 0] = [0, 0, 0]
cv2.imwrite("output/image_black_dot.png", img)

print("\nchange pixelset in image")
img = cv2.imread("../images/stacked1.png")
# img.itemset((150, 120, 0), 255)
img[150, 120, 0] = 0
cv2.imwrite("output/image_change_pixelset.png", img)

print("\nuse array slicing")
img_slicing = cv2.imread("../images/stacked1.png")
print("take all pixel from all rows/columns and set the green value")
img_slicing[:, :, 0] = 0
cv2.imwrite("output/image_array_slicing.png", img_slicing)

print("\nregions of interest (ROI)")
img = cv2.imread("../images/stacked1.png")
m_roi = img[0:50, 0:50]
img[100:150, 100:150] = m_roi
 # for illustration change 
img[100:150, 100:150, 0] = 255
img[100:150, 100:150, 2] = 0
cv2.imwrite("output/image_roi.png", img)

print("\naccess properties of numpy array")
img = cv2.imread("../images/stacked1.png")
print(image.shape)
print(image.size)
print(image.dtype)

print("\nfamiliarize with numpy")
print("- https://numpy.org/")
