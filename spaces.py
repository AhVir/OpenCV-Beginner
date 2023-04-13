import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread('Photos/park.jpg') ##openCV reads file in BGR format which is inverse of RGB
cv.imshow('Image', image)

# plt.imshow(image) ##but, matplotlib has no idea regarding that, and it reads file as RGB. So, it's thinking BGR as RGB
# # plt.show()   ##That's why, where is Blue, it's showing red and vice verse.

# #--> BGR to RGB (using OpenCV)
# rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# cv.imshow('RGB in CV', rgb)
# plt.imshow(rgb)
# plt.show()

# #---> BGR to GrayScale     (Conversion from Gray to HSV directly isn't possible, We need to go through BGR to do that)
gy = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gy)

# #---> BGR to HSV Format (HSV= Huge Saturation Value)
hssv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hssv)

# #---> BGR to LAB(L*A*B)
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)



##---> Inverse everything (like, gray->BGR, HSV->BGR and so on)

# #---> HSV to BGR
# hsv2bgr = cv.cvtColor(hssv, cv.COLOR_HSV2BGR)
# cv.imshow('Hsv2BGR', hsv2bgr)

# #--> LAB to BGR
# lab2bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow('LAB2BGR', lab2bgr)


##---> Gray to BGR
graytoBGR = cv.cvtColor(gy, cv.COLOR_GRAY2BGR)
cv.imshow('Gray2BGR', graytoBGR)


cv.waitKey(0)