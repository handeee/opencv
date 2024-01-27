import cv2
import numpy as np 

resim1=cv2.imread("cyilmaz.jpg")
resim2=cv2.imread("ozanguven.jpg")

cv2.imshow("cyilmaz",resim1)
cv2.imshow("ozanguven",resim2)

toplam=cv2.add(resim1,resim2)

cv2.imshow("toplandiresimler",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()