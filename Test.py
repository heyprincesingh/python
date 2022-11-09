import cv2

img = cv2.imread('D:\\Coding\\temp\\1.jpg')

clahe = cv2.createCLAHE()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

enh_img = clahe.apply(gray_img)

cv2.imwrite('D:\\Coding\\temp\\enhanced1.png',enh_img)

print('Enhancing successful')