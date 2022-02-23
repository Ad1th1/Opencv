
import cv2 as cv
import numpy as np

img=cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park',img)

#Translation - shift along x and y axes
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
#  x --> right
#  y --> down

translated=translate(img,100,100)
cv.imshow('Translated',translated)

translated=translate(img,-100,100)
cv.imshow('Translated again',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
cv.imshow('Rotated',rotated)

#rotated image of previously rotated image
rr=rotate(rotated,-45)
cv.imshow('Rotated again',rr)

rr=rotate(rotated,-90)
cv.imshow('Rotated again twice',img)

#Resizing an image
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping an image - 0(vertical),1(horizontal),-1(both)
flip=cv.flip(img,0)
cv.imshow('Flip1',flip) 

flip=cv.flip(img,1)
cv.imshow('Flip2',flip) 

flip=cv.flip(img,-1)
cv.imshow('Flip3',flip) 

#Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)