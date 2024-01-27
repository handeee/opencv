import cv2 
import numpy as np

resim=cv2.imread("turkansoray.jpg")
ikikatbuyuk=cv2.pyrUp(resim)
ikikatkucuk=cv2.pyrDown(resim)

print("orijinal resim",resim.shape)
print("iki kat buyuk resim ",ikikatbuyuk.shape)
print("iki kat kucuk resim",ikikatkucuk.shape)

cv2.imshow("orijinal resim",resim)
cv2.imshow("iki kat buyuk resim",ikikatbuyuk)
cv2.imshow("iki kat kucuk resim",ikikatkucuk)

cv2.waitKey(0)
cv2.destroysAllWindows()