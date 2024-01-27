import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    
    cv2.imshow("ozengineer",goruntu)
    
    if cv2.waitKey(30)& 0xFF==('q'):
        break
# 0xff yani çıkışım eşitse q harfine çıkış yap
#kameranın çalışıp çalışmadığını bilmek için ret kullanılır
#sürekli görüntü alınacak bizim belirlediğimiz sürede birleştiriyo
# bilgisayar kamersından bizi gösterir
kamera.release()
cv2.destroyAllWindows()