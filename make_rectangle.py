import glob
import numpy as np
import cv2
import imutils
from imutils import contours

from skimage import transform
from common import four_point_transform

path = './images/*'
file_list = glob.glob(path)
img_list = [file for file in file_list if file.endswith('.png')]

# print(img_list)

# for file in img_list:
#     print(file)

img = cv2.imread('images/pcb2.png')
img = imutils.resize(img, width=600)

# Converter into GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OutLine
edged = cv2.Canny(gray, 100, 255)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# edged = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow('edged', edged)
cv2.imshow('gray', gray)


# find contours in the edge map
cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

for cnt in cnts:
    print(cnt)
    # box = cv2.minAreaRect(cnt)
    # print(box)
    # box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)

    # (x,y, w,h) = rect
    # cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

# # FIND LARGEST CONTOURS
# rect = cv2.boundingRect(largest)
# (x,y, w,h) = rect
# cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

# # CROP
# cropped = img[y:y+h, x:x+w]

# box = cv2.minAreaRect(largest)
# box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
# box = box.astype('int')

# cv2.drawContours(img, [box], -1, (0, 255, 0), 2)
cv2.imshow('img', img)

# print(box)
# pts = box - box.min(axis=0)
# print(pts)

# dest3 = four_point_transform(cropped, pts)
# cv2.imshow('dest3', dest3)

cv2.waitKey(0)



