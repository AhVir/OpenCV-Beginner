import cv2 as cv


#Reading Images :-

# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow('A Cat', img)


#cv.waitKey(0)


#Reading Videos :-

vid = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vid.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()

cv.destroyAllWindows
