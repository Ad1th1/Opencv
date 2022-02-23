import cv2 as cv

#Reading pictures in opencv

img=cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)

#Graying an image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Canny edges
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

#contours, heirarchies
contours, heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

contours, heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)
