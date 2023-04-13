import cv2 as cv

video = cv.VideoCapture(0)

while True:
    isTrue, img = video.read()

    cv.imshow('Webcam', img)

    cv.waitKey(1)