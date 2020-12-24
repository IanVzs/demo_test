# -*- coding: utf-8 -*
"""
Created on Sat Jan 11 10:41:52 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('colors.png')
rows,cols,ch=img.shape
pts_befer = np.float32([[50,50],[200,50],[50,200]])
pts_after = np.float32([[10,100],[200,50],[100,200]])

=cv2.getAffineTransform(pts_befer,pts_after)
dst=cv2.warpAffine(img,M,(cols,rows))

#print(img)
plt.subplot(2,2,1)
plt.imshow(img)

plt.subplot(2,2,2)
plt.imshow(dst)

# plt.subplot(121,plt.imshow(img),plt.title('Input'))
# plt.subplot(121,plt.imshow(img),plt.title('Output'))

#plt.show()




# -*- coding: utf-8 -*
"""
Created on Sat Jan 11 10:51:19 2014
@author: duan
"""
# import cv2 
# import numpy as np 
# from matplotlib import pyplot as plt

img=cv2.imread('colors.png') 
rows,cols,ch=img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) 
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
=cv2.getPerspectiveTransform(pts1,pts2) 
dst=cv2.warpPerspective(img,M,(300,300))

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(dst)

plt.show()
