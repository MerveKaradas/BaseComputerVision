#KAYNAK : https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

import cv2

#orjinal resim
img = cv2.imread('opencv.jpg')
cv2.imshow('OpenCV ORJINAL', img)

# Averaging blur
blur = cv2.blur(img,(9,9)) #blur tek ve çift sayıları alır
cv2.imshow('OpenCV Blur',blur)

# Gaussian blur
gaussian = cv2.GaussianBlur(img,(9,9),0) # gaussian sadece tek sayıları alır
cv2.imshow('OpenCV Gaussian Blur',gaussian)

# Median Blurring
median = cv2.medianBlur(img,9)
cv2.imshow('OpenCV Median Blur',median)

# Bilateral
bilateral = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('OpenCV Bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
