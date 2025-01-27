import cv2
import os

if not os.path.exists("output"):
    os.mkdir("output")

face_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')
img = cv2.imread('../images/woodcutters.jpg')
# cacade clasifier expects grayscale images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# fun 1.01 / 20 - detects mulitple faces even in trees
# fun 1.08 / 5 - detects the optimum of faces 3 of 5
scale_factor = 1.08 # should be greater than 1.0 
min_neighbors = 5
faces = face_cascade.detectMultiScale(gray, scale_factor, min_neighbors)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
  
cv2.imshow('Woodcutters Detected!', img)
cv2.imwrite('./output/woodcutters_detected.png', img)
cv2.waitKey(0)
