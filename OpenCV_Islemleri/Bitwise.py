import cv2

bitwise1 = cv2.imread('images/bitwise1.png')
bitwise2 = cv2.imread('images/bitwise2.png')

cv2.imshow('bitwise1', bitwise1)
cv2.imshow('bitwise2', bitwise2)

print("bitwise1 shape : ", bitwise1.shape)
print("bitwise2 shape : ", bitwise2.shape)

#Eğer resimler aynı boyutta değillerse hata verecektir o yüzden boyutlarını aynı yapıyoruz
bitwise1 = cv2.resize(bitwise1, (350, 575))
bitwise2 = cv2.resize(bitwise2, (350, 575))

bitwise_or = cv2.bitwise_or(bitwise1, bitwise2)
cv2.imshow('bitwise_or', bitwise_or)

bitwise_and = cv2.bitwise_and(bitwise1, bitwise2)
cv2.imshow('bitwise_and', bitwise_and)

bitwise_xor = cv2.bitwise_xor(bitwise1, bitwise2)
cv2.imshow('bitwise_xor', bitwise_xor)

bitwise1_not = cv2.bitwise_not(bitwise1)
bitwise2_not = cv2.bitwise_not(bitwise2)
cv2.imshow('bitwise1_not', bitwise1_not)
cv2.imshow('bitwise2_not', bitwise2_not)


cv2.waitKey(0)
cv2.destroyAllWindows()
