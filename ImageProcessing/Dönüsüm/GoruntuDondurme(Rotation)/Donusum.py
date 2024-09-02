import cv2

image = cv2.imread('../img.png')
cv2.imshow('Orjinal Resim', image)

# Görüntü boyutları
(h, w) = image.shape[:2]

# Döndürme merkezi (görüntünün merkezi)
center = (w // 2, h // 2)

# Döndürme matrisi oluşturma (45 derece döndürme)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# Görüntüyü döndürme
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow('Dondurulmus resim', rotated_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
