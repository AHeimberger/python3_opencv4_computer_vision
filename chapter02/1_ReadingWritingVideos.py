import cv2
import os

if not os.path.exists("output"):
    os.mkdir("output")

print("\n3x3 capture and write video")
videoCapture = cv2.VideoCapture("../videos/pedestrians.avi")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("- codecs I420: https://learn.microsoft.com/en-us/windows/win32/medfound/video-fourccs")
videoWriter = cv2.VideoWriter("output/video.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()
