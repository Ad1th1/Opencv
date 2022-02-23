import cv2 as cv

img=cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

#Convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#To increase Blur
blurrr=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blurrier',blurrr)

#Edge Cascade - blurring and gradient computations
canny  = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

#Edge Cascade on blurred image- blurring and gradient computations
canny  = cv.Canny(blurrr,125,175)
cv.imshow('Canny Edges',canny)

#Dilate the edges
dilated  = cv.dilate(img,(3,3),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)


#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

#Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

#Translation = shift an image up or down
def translate()
 

cv.waitKey(0)