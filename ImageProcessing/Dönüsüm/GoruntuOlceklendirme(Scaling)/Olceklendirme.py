import cv2


image = cv2.imread('../img.png')
cv2.imshow('Orjinal Resim', image)

# Ölçeklendirme faktörleri (genişlik ve yükseklik için)
scale_x = 1.5  # Genişlikte %150 büyütme
scale_y = 1.5  # Yükseklikte %150 büyütme

# Ölçeklendirme işlemi
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Olceklendirilmis Resim', scaled_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
