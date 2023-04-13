import cv2 as c

img = c.imread('Photos/cats.jpg')
c.imshow('Image', img)

gray = c.cvtColor(img, c.COLOR_BGR2GRAY)
c.imshow('Gray', gray)

c.imwrite('Photos/Gray_cat.jpg', gray)

c.waitKey(0)