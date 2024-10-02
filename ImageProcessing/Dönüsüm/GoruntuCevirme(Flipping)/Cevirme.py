import cv2

image = cv2.imread('../img.png')

# Yatay çevirme
flipped_horizontally = cv2.flip(image, 1)

# Dikey çevirme
flipped_vertically = cv2.flip(image, 0)

# Hem yatay hem dikey çevirme
flipped_both = cv2.flip(image, -1)


cv2.imshow('Orjinal Resim', image)
cv2.imshow('Yatay Cevirme', flipped_horizontally)
cv2.imshow('Dikey Cevirme', flipped_vertically)
cv2.imshow('Hem Yatay Hem Dikey Cevirme', flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
