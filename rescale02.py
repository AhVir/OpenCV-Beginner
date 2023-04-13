import cv2 as cv

def rescale(frame, scale=.75):
    height = int(frame.shape[0] * scale)
    weight = int(frame.shape[1] * scale)

    dimension = (weight, height)
    # dimension = (height, weight)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# im = cv.imread('Photos/cat_large.jpg')
# cv.imshow('new window', im)

# re_image = rescale(im)
# cv.imshow('resized_Image', re_image)

# cv.waitKey(0)

vd = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, fr = vd.read()

    cv.imshow('Video', fr)

    re_frame = rescale(fr, scale = .20)
    cv.imshow('Rescaled Video', re_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.release
cv.destroyAllWindows