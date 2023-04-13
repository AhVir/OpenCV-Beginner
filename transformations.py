import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


# #----> Translation

# def translation(image, x, y):
#     transMat = np.float32([[1,0,x], [0,1,y]])
#     dimension = (image.shape[1], image.shape[0])
#     return cv.warpAffine(image, transMat, dimension)

# # x ---> Right
# # y ---> Down
# #-y ---> Up
# #-x ---> Left

# trans = translation(img, 100, -100)
# cv.imshow('Translated', trans)


# #----> Rotation

# def rotation(image, angle, rotationPoint=None):
#     (height, width) = image.shape[0], image.shape[1]   ## Could be written as (height, width) = image.shape[:2]

#     if rotationPoint is None: #we are going to assume that we want to rotate in center
#         rotationPoint = (width//2, height//2)

#     rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
#     dimen = (width, height)

#     return cv.warpAffine(image, rotationMatrix, dimen)

# rotate = rotation(img, -160)  #angle will be in degrees
# cv.imshow("ROtation", rotate)

# again_rotate = rotation(img, 120)
# cv.imshow("Again-Rotated", again_rotate)


# #---> Resizing

# resize = cv.resize(img, (400, 425), interpolation=cv.INTER_AREA)
# cv.imshow("Resized Park", resize)

# #---> Flipping

# ##flip codes:
# # 0 = flipping the image vertically that is over the X axis
# # 1 = flipping the image horizontally or over the Y axis
# # -1 = flipping the image both vertically as well as horizontally

# flipping0 = cv.flip(img, 0)
# flipping1 = cv.flip(img, 1)
# flippingMinus1 = cv.flip(img, -1)

# cv.imshow('Flipping 0', flipping0)
# cv.imshow('Flipping 1', flipping1)
# cv.imshow('Flipping -1', flippingMinus1)


#---> Cropping

cropping = img[200:400, 300:400]
cv.imshow('Cropped', cropping)

cv.waitKey(0)