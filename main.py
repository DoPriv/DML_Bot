import cv2 as cv
import ADB_Server
import window
import windowCapture

# ADB = ADB_Server.ADB("emulator-5554")  # Check if the game is installed or not and start the game if it is so.
# if ADB.getStatus() != 0:
#     exit(1)

# Reposition Emulator window to x-0 y-0
emulatorWindow = window("LDPlayer")

#window = windowCapture.WindowCapture("LDPlayer")
#cv.imshow("img",window.get_screenshot())
cv.waitKey()
