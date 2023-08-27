import cv2 as cv
import sys
img = cv.imread(r'C:\Users\HP\Pictures\Saved Pictures\i1.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (960, 540))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    print(cv.imwrite(r'C:\Users\HP\Pictures\Saved Pictures\venice.jpg', img))