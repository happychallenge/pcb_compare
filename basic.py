# import the necessary packages
from skimage.metrics import structural_similarity
from common import order_points, four_point_transform
import argparse
import imutils
import cv2

img = cv2.imread('images/pcb2.png')

img = imutils.resize(img, width=800)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

_, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

cv2.imshow('Thres', thresh)
cv2.waitKey(0)