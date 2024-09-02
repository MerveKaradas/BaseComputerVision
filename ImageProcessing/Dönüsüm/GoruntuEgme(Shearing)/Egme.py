import cv2
import numpy as np

image = cv2.imread('../img.png')
cv2.imshow('Orjinal Resim', image)

# Görüntü boyutları
(h, w) = image.shape[:2]

# Eğme (shearing) matrisi oluşturma (x ekseninde eğme)
shear_matrix = np.float32([[1, 0.5, 0],
                           [0.5, 1, 0]])

# Görüntüyü eğme (warpAffine kullanarak)
sheared_image = cv2.warpAffine(image, shear_matrix, (int(w * 1.5), int(h * 1.5)))

cv2.imshow('Egilmis Resim', sheared_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
