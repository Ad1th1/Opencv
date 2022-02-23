import cv2 as cv
import numpy as np

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Paint range of an image a certain color
blank[200:300,300:400]=0,255,0
cv.imshow('Red,again',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Paint the image a certain color
blank[:]=0,255,0
cv.imshow('Green',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

blank[:]=0,0,255
cv.imshow('Red',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,255),thickness=2)
cv.imshow('Rectangle',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,255),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Draw a cicle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#blank ->height,width,number of color channels
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Writing text
cv.putText(blank,'Hello, my name is Adithi!',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)
