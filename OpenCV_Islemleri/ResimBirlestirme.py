"""""
Birleştirme yapacağımız görsellerin aynı boyutta olması lazım çünkü biz matrisleri 
toplamış oluyoruz ve matris toplamlarında boyutların aynı olması gereklidir"""""
import cv2
import numpy as np

img_opencv = cv2.imread('images/opencv.jpg')
img_pycharm = cv2.imread('images/pycharm.png')

# boyut kontrolü
print("ilk pycharm boyutu : ",img_pycharm.shape)
print("ilk opencv boyutu : ",img_pycharm.shape)

# aynı boyutta olmadığından aynı boyut olacak şekilde ayarlama
img_pycharm = cv2.resize(img_pycharm, (200, 200))
img_opencv = cv2.resize(img_opencv, (200, 200))

print("son pycharm boyutu : ",img_pycharm.shape)
print("son opencv boyutu : ",img_pycharm.shape)

cv2.imshow("pycharm", img_pycharm)
cv2.imshow("opencv", img_opencv)


#Birleştirme İşlemi
birlestirilenGörsel = cv2.add(img_pycharm, img_opencv)
cv2.imshow("birlestirme", birlestirilenGörsel)

print("pycharmın nokta renkleri",img_pycharm[150,150])
print("opencnin nokta renkleri",img_opencv[150,150])
print("birlestirme nokta renkleri",birlestirilenGörsel[150,150])

#Ağırlıklı Toplama
agirlikliGorsel = cv2.addWeighted(img_pycharm, 0.5, img_opencv, 0.5, 0)
cv2.imshow("Agirlikli Gorsel", agirlikliGorsel)

cv2.waitKey(0)
cv2.destroyAllWindows()
