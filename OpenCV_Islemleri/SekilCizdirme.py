import cv2
import numpy as np


tuval = np.zeros((600, 600, 3), np.uint8) + 255 #boş bir tuval oluşturma


# İÇİ DOLU KARE
cv2.rectangle(tuval, (100, 100), (300, 300), (0, 0, 255), -1) # -1 ile içerisini dolduruyoruz

# DİKDÖRTGEN
cv2.rectangle(tuval, (350, 350), (500, 450), (255, 0, 0))

# YUVARLAK
cv2.circle(tuval, (100, 450), 50, (55, 200, 100), -1)

# ÇİZGİ
cv2.line(tuval, (380, 20), (450, 200), (0, 0, 0),4)

# BOŞ ÜÇGEN
u1 = (250,400)
u2 = (250,450)
u3 = (400,550)

cv2.line(tuval, u1, u2, (255, 0, 0), 2)
cv2.line(tuval, u1, u3, (255, 0, 0), 2)
cv2.line(tuval, u2, u3, (255, 0, 0), 2)

# DOLU ÜÇGEN
points = np.array([[330, 200], [330, 330], [500, 330]])
cv2.fillPoly(tuval, [points], (100,0 , 100))


# Şekilleri Gösterme
cv2.imshow("Sekil Cizimleri",tuval)
cv2.waitKey(0) # sonsuz bir süre boyunca tuşa basılmasını bekler.(0 parametresi için)
cv2.destroyAllWindows() #tüm açık OpenCV pencerelerini kapatır

