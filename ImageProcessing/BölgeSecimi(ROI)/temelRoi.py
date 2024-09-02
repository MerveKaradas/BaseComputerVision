#Bölge Seçimi (ROI): Görüntüden belirli bir bölgeyi seçme ve işlemler uygulama.
"""ROI genellikle dört temel parametre ile tanımlanır:

x: ROI'nin sol üst köşesinin yatay koordinatı.
y: ROI'nin sol üst köşesinin dikey koordinatı.
w: ROI'nin genişliği.
h: ROI'nin yüksekliği."""

import cv2
import numpy as np

#Görüntüyü okuma
img = cv2.imread('opencv.jpg')

#Görüntü boyutlarını alma
height, width, channels = img.shape #shape boyutları döndürür
print(f"height : {height} width : {width} channels : {channels}")

#Görüntüyü gösterme
cv2.imshow('image', img)

#Belirli bir pixel noktasının renkleri
colors = img[88,110]
print(colors)
print(f"blue {img[88,110,0]} green {img[88,110,1]} red {img[88,110,2]}")

#pixel rengini değiştirmek istersek
old_blue =img.item(88,110,0) # (88,110) noktasının mavi değeri
print(f"Değişmeden önce blue : {old_blue}")

img[88,110,0] = 200 # (88,110) noktasının mavi değeri 200 değeri ile değiştirildi
new_blue = img.item(88,110,0) # (88,110) noktasının mavi değeri
print(f"Değiştirdikten sonra blue : {new_blue}")

# ROI
roi = img[100:200 , 100:210]
cv2.imshow('roi', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()