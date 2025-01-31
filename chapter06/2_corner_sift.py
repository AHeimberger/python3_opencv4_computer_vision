import cv2

red = (0, 0, 255)
img = cv2.imread('../images/varese.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)

# cv2.drawKeypoints(img, keypoints, img, red, cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
cv2.drawKeypoints(img, keypoints, img, red, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.drawKeypoints(img, keypoints, img, red, cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('sift_keypoints', img)
cv2.waitKey()
