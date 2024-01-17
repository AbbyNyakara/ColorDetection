# Import the opencv library
import cv2 as cv

# Create the videocapture object.
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open the video")
    exit()
#vid.read(): This method reads the next video frame from the video source (vid).
#It returns two values: a boolean ret and the actual frame data frame.
while True:
    ret, frame = cap.read()

    # display the frame:
    cv.imshow("Frame", frame)

    # Wait for a key event to exit the loop:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()

# Destroy all windows:
cv.destroyAllWindows()
