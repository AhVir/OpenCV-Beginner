import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #will work for everything,like Images, Videos & Live Video
    height = int(frame.shape[0] * scale)
    weight = int(frame.shape[1] * scale)

    dimen = (weight, height)

    return cv.resize(frame, dimen, interpolation=cv.INTER_AREA)


#cv.waitKey(0)


#Reading Videos :-

vid = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vid.read()

    re_frame = rescaleFrame(frame, scale =.20)

    cv.imshow('Video', frame)
    cv.imshow('Video Which is resized', re_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()

# This changeRes function will Work for only Live Video
def changeRes(width, height):
    frame.set(3,width)
    frame.set(4,height)

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Window', img)

re_img = rescaleFrame(img, scale=.2)
cv.imshow('rescale', re_img)

cv.waitKey(0)

cv.destroyAllWindows