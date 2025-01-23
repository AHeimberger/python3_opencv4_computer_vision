import cv2
import numpy as np

img = cv2.imread('../images/hough_lines.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
# cdst = img.copy()
cdstP = img.copy()

blue = (255, 0, 0)
green = (0, 255, 0)
threshold=20
minLineLength = 30
maxLineGap = 5

# points = cv2.HoughLines(edges,
#                         rho=1,
#                         theta=np.pi/180.0,
#                         threshold=threshold)
# for point in points:
#     rho, theta = point[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho; y0 = b*rho
#     x1 = round(x0 + 20*(-b)); y1 = round(y0 + 20*(a))
#     x2 = round(x0 - 20*(-b)); y2 = round(y0 - 20*(a))
#     cv2.line(cdst, (x1, y1), (x2, y2), blue, 2)

lines = cv2.HoughLinesP(edges,
                        rho=1,
                        theta=np.pi/180.0,
                        threshold=threshold,
                        minLineLength=minLineLength,
                        maxLineGap=maxLineGap)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(cdstP, (x1, y1), (x2, y2), green, 2)

cv2.imshow("gray", gray)
cv2.imshow("edges", edges)
# cv2.imshow("cdst", cdst)
cv2.imshow("cdstP", cdstP)
cv2.waitKey()
cv2.destroyAllWindows()
