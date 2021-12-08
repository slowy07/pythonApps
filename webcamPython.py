import cv2

capture = cv2.VideoCapture(0)

framesWidth = int(capture.get(3))
framesHeight = int(capture.get(4))

fourcc = cv2.VideoWriter_fourcc(*"MJPG")
output = cv2.VideoWriter("recording.avi", fourcc, 20.0, (framesWidth, framesHeight))

while True:
    ret, frame = capture.read()
    if ret == True:
        output.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)
        if cv2.waitKey(1) and 0xFF == ord("q"):
            break

# CREATE
capture.release()
output.release()
cv2.destroyAllWindows()
