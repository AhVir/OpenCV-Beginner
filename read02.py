import cv2 as cv

# image = cv.imread('photos/cats 2.jpg')

# cv.imshow('A cool new window', image)

# cv.waitKey(0)

video = cv.VideoCapture('Videos/kitten.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('A way more cooler Window', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows