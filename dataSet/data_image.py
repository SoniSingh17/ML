import cv2

img = cv2.imread("images/cat.jpg")     # local file path
print(img.shape)                         # (H, W, C)
