import numpy as np
import cv2 as cv
cap = cv.VideoCapture(r'C:\Users\HP\Pictures\Saved Pictures\video.avi')
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(r'C:\Users\HP\Pictures\Saved Pictures\copy.avi', fourcc, 20.0, (960, 540))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)
 # write the flipped frame
    out.write(frame)
    cv.imshow('cpy video', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()