# Import the opencv library
import cv2 as cv
from utils import get_limits

# Create the videocapture object.
# by passing 0, it will capture the default camera
cap = cv.VideoCapture(0)

# Yellow in BGR Colorspace
yellow  = [0, 255, 255]
if not cap.isOpened():
    print("Unable to open the video")
    exit()
#vid.read(): This method reads the next video frame from the video source (vid).
#It returns two values: a boolean ret and the actual frame data frame.
while True:
    isTrue, frame = cap.read()

    # Convert the default BGR TO HSV
    hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    # display the frame:
    cv.imshow("Frame", frame)

    # Wait for a key event to exit the loop:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()

# Destroy all windows:
cv.destroyAllWindows()
