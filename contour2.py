import cv2 as cv
import numpy as np

#Reading pictures in opencv
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cat',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

#Graying an image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Canny edges
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

# thresholding - to binarize an image
ret,thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

#contours = kinda like edges, heirarchies
contours, heirarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found! on thresh')

#draw contours on the blank page
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours drawn',blank)

#contours = kinda like edges, heirarchies
contours, heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found! on canny')

#draw contours on the blank page
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours drawn',blank)



cv.waitKey(0)
