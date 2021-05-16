import numpy as np
import cv2
#a = str(10879)
for i in range(1,2921):
    img=cv2.imread('/home/ctam/Desktop/imageAugmentation/normalimage/nimage'+str(i)+'.JPEG')
    num_rows, num_cols = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -30, 1)
    img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
    cv2.imshow('Rotation', img_rotation)
    cv2.imwrite("/home/ctam/Desktop/imageAugmentation/rotatedimage/r-image"+str(i)+".JPEG",img_rotation)

cv2.waitKey(0)
cv2.destroyAllWindows()
