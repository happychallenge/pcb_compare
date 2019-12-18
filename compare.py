# import the necessary packages
from skimage.metrics import structural_similarity
from common import order_points, four_point_transform
import argparse
import imutils
import cv2

first = cv2.imread('data/pcb4.png')
second = cv2.imread('data/pcb4bak.png')

second = imutils.resize(second, width=first.shape[1])

second = imutils.resize(second, width=first.shape[1])
grayFirst = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
graySecond = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

## First Picture Crop Method
edged = cv2.Canny(grayFirst, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

largest = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
(x,y, w,h) = cv2.boundingRect(largest)
origin = first[y:y+h, x:x+w]
grayFirst = grayFirst[y:y+h, x:x+w]


## Second Picture Crop Method
edged = cv2.Canny(graySecond, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

largest = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
(x,y, w,h) = cv2.boundingRect(largest)
second = second[y:y+h, x:x+w]
graySecond = graySecond[y:y+h, x:x+w]

(score, diff) = structural_similarity(grayFirst, graySecond, full=True)
diff = (diff * 255).astype('uint8')
print("SSIM: {}".format(score))

thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

for c in cnts:
    (x,y, w,h) = cv2.boundingRect(c)
    cv2.rectangle(second, (x,y), (x+w, y+h), (0,0,255), 4)

second = imutils.resize(second, width=1024)
cv2.imshow('Second', second)
# cv2.imshow('Diff', diff)
# cv2.imshow('Thresh', thresh)
cv2.waitKey(0)