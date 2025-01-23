import cv2
import os

if not os.path.exists("output"):
    os.mkdir("output")

print("\n3x3 capture a 10s video from the camera")
videoCapture = cv2.VideoCapture(0)
fps = 30 # assumption
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("- codecs I420: https://learn.microsoft.com/en-us/windows/win32/medfound/video-fourccs")
videoWriter = cv2.VideoWriter("output/video.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

success, frame = videoCapture.read()
numFramesRemaining = 10 * fps - 1 # 10 seconds of frames
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = videoCapture.read()
    numFramesRemaining -= 1
