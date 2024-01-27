import cv2

#mean ort filtre daha bozuk görüntü
#

image=cv2.imread("resim.webp")
meanFilter=cv2.blur(image,(3,3))
meanFilter2=cv2.blur(image,(5,5))


medianfilter=cv2.medianBlur(image,3)
medianFilter2=cv2.medianBlur(image,5)

cv2.imshow("orijinal resim",image)
cv2.imshow("mean filter 3*3",meanFilter)
cv2.imshow("mean filter 5*5",meanFilter2)
#median filter daha orijinal,mean daha yumuşak

cv2.imshow("median filter ",medianfilter)
cv2.imshow("median filter ",medianFilter2)

#gauss fılterıng
#görüntüyü bulanıklaştırarak gürültüyü ortadan kaldırmak için kullanılır çan eğrisi şeklinde

gauss=cv2.GaussianBlur(image,(3,3),0)

cv2.imshow("gauss filter",gauss)






cv2.waitKey(0)
cv2.destroyAllWindows()