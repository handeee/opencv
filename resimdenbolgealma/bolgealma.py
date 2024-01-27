import cv2 
import numpy as np

resim=cv2.imread("fish.png")



kesit=resim[50:100,50:100]

resim[0:50,0:50]=kesit
resim[0:50,0:50,1]=255
resim[0:50,0:50,0]=500
resim[0:50,0:50,2]=200

cv2.imshow("balik",resim)




cv2.waitKey(0)
cv2.destroyAllWindows()
