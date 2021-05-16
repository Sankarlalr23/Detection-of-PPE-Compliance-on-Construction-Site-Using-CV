import numpy as np
import cv2
#a = str(10879)
for i in range(1,2921):
    img=cv2.imread('/home/ctam/Desktop/imageAugmentation/name/nimage'+str(i)+'.JPEG')
    rimg=img.copy()
    rimg=cv2.flip(img,1)
#fimg=cv2.flip(img,0)
#cv2.imshow("Original", img)
#cv2.imshow("vertical flip", rimg)
    cv2.imwrite("/home/ctam/Desktop/imageAugmentation/name1/vimage"+str(i)+".JPEG",rimg)
#cv2.imshow("horizontal flip", fimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
