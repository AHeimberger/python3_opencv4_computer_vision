import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow("MyWindow")
cv2.setMouseCallback("MyWindow", onMouse)

print("Showing camera feed. Click window or press any key to stop")
success, frame = cameraCapture.read()
# waitkey per default is 0 which means infinite
# return value -1 means no key presssed
# return value 27 means esc pressed
# ord('a') converts to 97
print("- www.asciiitable.com for return vlaues")
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("MyWindow", frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow("MyWindow")
cameraCapture.release()
