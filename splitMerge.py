import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blnk = np.zeros(img.shape[:2], dtype='uint8')

blue, green, red = cv.split(img)

blue_ = cv.merge([blue, blnk, blnk])
green_ = cv.merge([blnk, green, blnk])
red_ = cv.merge([blnk, blnk, red])

# print(img)  ##Actual BGR image has 3 shapes(B,G,R)
# print(red)  ##gray scaled image has a shape of 1, also that's why will show a grayscaled image for all these 3
# print(green)
# print(blue)

# cv.imshow('Blue', blue)
# cv.imshow('Red', red)
# cv.imshow('Green', green)


##Now, let's merge all these 3 colour channels
merged_imaged = cv.merge([blue, green, red])  ## [] => indicates list in python
cv.imshow('Merged-Image', merged_imaged)

cv.imshow('Blue_', blue_)
cv.imshow('Green_', green_)
cv.imshow('Red_', red_)

bluee = cv.split(blue_)
cv.imshow('Blueeeeeee', bluee[0])

greenn = cv.split(green_)
cv.imshow('Greennn', greenn[1])

redd = cv.split(red_)
cv.imshow('Reddd', redd[2])

merge_merge_image = cv.merge([bluee[0], greenn[1], redd[2]])
cv.imshow('Merge-merged Image', merge_merge_image)


cv.waitKey(0)