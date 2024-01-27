import cv2
import numpy as np

resim=cv2.imread("fish.png")

aynalananresim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
uzatilanresim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarresim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_WRAP)
sarilanresim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_CONSTANT,value=(75,150,255))




cv2.imshow("aynalanan balik",aynalananresim)
cv2.imshow("uzatılan balik",uzatilanresim)
cv2.imshow("tekrarlanan balik",tekrarresim)
cv2.imshow("lan balik",sarilanresim)

cv2.waitKey(0)
cv2.destroysAllWindows()