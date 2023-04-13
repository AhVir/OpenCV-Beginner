import cv2

img = cv2.imread('Photos/bgr_image.jpg')

cv2.imshow('Hi', img)
cv2.waitKey(0)
