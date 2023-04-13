import cv2 as cv
import numpy as np

blnk = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank Image', blnk)

img = cv.imread('Photos/Cat.jpg')

# cv.imshow('Interesting Image', img)


#1. Paint the image a certain colour
# blnk[:] = 0,255,0
# cv.imshow('Green', blnk)

# blnk[:] = 0,0,255
# cv.imshow('Red', blnk)

# blnk[:] = 255,0,0
# cv.imshow('Blue', blnk)

# blnk[200:300, 300:400] = 0,0,255
# cv.imshow('Draw', blnk)



#------------------>2. Draw a Rectangle
# cv.rectangle(blnk, (0,0), (250, 250), (0,255,0), thickness=4)
# cv.rectangle(blnk, (125, 125), (375,375), (0,0,255), thickness=100)

# Half is Red and Other half is Green

# cv.rectangle(blnk, (0,0), (250, 500), (0,255,0), thickness=cv.FILLED)
# cv.rectangle(blnk, (250, 0), (500, 500), (0, 0, 255), thickness=-1)


# cv.rectangle(blnk, (0,0), (blnk.shape[1]//2, blnk.shape[0]//2), (0,255,0), thickness=-1)
# cv.rectangle(blnk, (0,0), (blnk.shape[1]//2, blnk.shape[0]), (0,255,0), thickness=-1)



#------------------->3. Draw a Circle

# cv.circle(blnk, (250, 250), 80, (0,0,255), thickness=-1)
cv.circle(blnk, (blnk.shape[1]//2, blnk.shape[0]//2), 80, (0,0,255), thickness=cv.FILLED)


#------------------->4. Draw a line
cv.line(blnk, (250,0), (blnk.shape[1]//2, blnk.shape[0]//2), (255, 255, 0), thickness=3)
cv.line(blnk, (100, 100), (300, 450), (0,255, 255), thickness=5)


#-------------------->5. Write Te75
cv.putText(blnk, 'Hello Dude', (100, 100), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 59), thickness=2)
cv.putText(blnk, 'What\'s up, how are you doing?!?', (25, 200), cv.FONT_HERSHEY_TRIPLEX, .75, (255, 255, 59), thickness=2)
cv.putText(blnk, 'I\'m great, and you?!?', (25, 300), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 255, 59), thickness=2)
cv.putText(blnk, 'Alhamdulillah, Thanks for asking!', (25, 400), cv.FONT_HERSHEY_TRIPLEX, .70, (255, 255, 59), thickness=2)

cv.imshow("Rectangle", blnk)

cv.waitKey(0)