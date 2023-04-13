import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Image', img)

blnk = np.zeros(img.shape, dtype='uint8')   #img.shape[:2] --> takes first 2 values of img, for example, shape[0](height) & shape[1](width). Gave Error, now it's only img.shape
cv.imshow('Blank', blnk)  #img.shape[:2] --> to create blank image of same dimention

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)   ##125 --> threshold value(if it's below that, it will be considered as zero or blank), 255--> maximum(if it's above 125, it will be set to white or 255).
## "thresholding attempts to binarize an image.""
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blnk, contours, -1, (0,0,255), 1)   #contourIdx --> how many contours I want? '-1' means I want all of them.
cv.imshow('Contours Drawn', blnk)

cv.waitKey(0)