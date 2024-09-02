import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('images/opencv.jpg')

# Renk aralığını tanımla (Bu örnek, mavi renk için bir aralık)
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Görüntüyü HSV renk uzayına dönüştür
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Belirli renk aralığını maskelemek için maske oluştur
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Maskeyi orijinal görüntüyle birleştir
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
