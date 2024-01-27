import cv2
import numpy as np

resim=cv2.imread("resim.jpg")

resim[50,30]=[255,255,255]
("50px soldan aşağı,sağdan 30 pixel anlamında beyaz rengi atadık")

for i in range(100):
   resim[70,i]=[255,255,255] 
cv2.imshow("ev",resim)
      
cv2.waitKey(0)
cv2.destroyAllWindows()