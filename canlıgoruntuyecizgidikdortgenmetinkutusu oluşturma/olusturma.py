import cv2
import numpy as np 

resim=np.zeros((300,300,3),dtype="uint8")
# 300 yükseklik 300 genişlik 3 kanallı bölge oluştu
cv2.line(resim,(0,0),(100,100),(20,60,255),3)
# çizgi 0,0 dan başlasın 100,100 e kadar gitsin renk ve kalınlık

cv2.circle(resim,(150,150),25,(0,255,0),2)
#daire merkezi 150 ye 150 kesişimi, yarıçaapı 25

cv2.putText(resim,"OZGE KURT",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
# 100 sağa,aşağı 200 
#metnim ozge kurt, yazının başlangıç pikseli 200,200,yazıtipi özelliği,yazı boyutu 1,renk,kalınlık

cv2.imshow("deneme ",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()