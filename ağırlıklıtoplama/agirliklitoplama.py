import cv2 
import numpy as np

resim1=cv2.imread("emelsayin.jpg")
resim2=cv2.imread("turkansoray.jpg")

print(resim1[320,270])
print(resim2[300,450])

cv2.imshow("emel sayın",resim1)
cv2.imshow("turkan soray",resim2)

print(resim1[10,10]+resim2[300,430])

cv2.waitKey(0)
cv2.destroyAllWindows()

