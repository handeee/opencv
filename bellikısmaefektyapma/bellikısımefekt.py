import cv2 
import numpy as np 

ucgenresmi=cv2.imread("logo.png")
ucgenresmi[:,:,0]=255
cv2.imshow("ucgen resmi",ucgenresmi)



cv2.waitKey(0)
cv2.destroyAllWindows()