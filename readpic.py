import cv2 as cv

#Reading pictures in opencv

img=cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat',img)

cv.waitKey(0)
