import cv2 as cv

def rescale(frame, scale = .75):
    height = int(frame.shape[0] * scale)
    weight = int(frame.shape[1] * scale)

    dimen = (weight, height)

    return cv.resize(frame, dimen, interpolation=cv.INTER_AREA)

ig = cv.imread('Photos/park.jpg')

# # ig = rescale(img, scale=.25)

# cv.imshow('Image', ig)

# #===> 1. Converting to Gray Scale
# gray = cv.cvtColor(ig, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

# #===> 2. Blur
# blr = cv.GaussianBlur(ig, (7, 7), cv.BORDER_DEFAULT) #Ksize(kernal size) always needs to be in odd numbers
# cv.imshow('Blur Image', blr)

# #===> 3. Edge Cascade
# canny_edge_cascade = cv.Canny(ig, 125, 175)
# cv.imshow('Canny Cascade(Edging)', canny_edge_cascade)
# #edge cascading the blur one
# canny_edge_cascade_blur = cv.Canny(blr, 125, 175)
# cv.imshow('Canny Cascade(Edging)-Blur', canny_edge_cascade_blur)

# #===> 4. Dilating the Image
# dilated = cv.dilate(canny_edge_cascade_blur, (7, 7), iterations=1)
# cv.imshow('Dilated-Blur', dilated)

# #===> 5. Eroding
# eroded_blur = cv.erode(dilated, (7,7), iterations=1)
# cv.imshow('Enroded-blur', eroded_blur)


# # ===> 6. Resize (function Actually)
# image = cv.imread('Photos/cat_large.jpg')
# resized = cv.resize(image, (500, 400))  #this aspect ratio indicates in which size you want to see the image, like in how much pixel
# cv.imshow('Resize Function', resized)

# park = cv.imread('Photos/park.jpg')
# park_resize1 = cv.resize(park, (500, 400), interpolation=cv.INTER_CUBIC) #used to enlarge the image, it's the slowest among them, but the image is of much higher quality
# park_resize2= cv.resize(park, (500, 400), interpolation=cv.INTER_AREA)   #used to shrink the image
# park_resize3 = cv.resize(park, (500, 400), interpolation=cv.INTER_LINEAR) #used to enlarge the image

# cv.imshow('park1', park_resize1)
# cv.imshow('park2', park_resize2)
# cv.imshow('park3', park_resize3)

#===> 7. Cropping  //Consider it as an array, and using a slice of it on a basis of the pixel value
cropped_image = ig[50:200, 200:400]
cv.imshow('Original Imgae', ig)
cv.imshow('Cropped Image', cropped_image)


cv.waitKey(0)