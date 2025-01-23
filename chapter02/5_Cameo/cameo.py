import cv2
import os
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager("Cameo", self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """Run the main loop"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                #TODO: Filter the frmae (chapter 3)
                pass
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    
    def onKeypress(self, keycode):
        """Handle a keypress. 
        space -> take a screenshot
        tab -> start/stop recording a screencast
        escape -> quit"""
        if not os.path.exists("output"):
            os.mkdir("output")

        if keycode == 32:
            self._captureManager.writeImage("output/cameo_screenshot.png")
        if keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo("output/camoe_screencast.avi")
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()
