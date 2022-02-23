#Resizing and Rescaling video

import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    #works for images, videos and live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #works only for live videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue,frame =capture.read()

    frame_resized = rescaleFrame(frame,scale=0.75)

    frame_resized2 = rescaleFrame(frame,scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    cv.imshow('Video Resized Again',frame_resized2)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

img=cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

resized_image = rescaleFrame(img)
cv.imshow('Resized Image',resized_image)

cv.waitKey(0)

cv.waitKey(0)