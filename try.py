import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()



    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv.destroyAllWindows()