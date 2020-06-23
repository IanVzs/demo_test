import cv2
import copy
import numpy as np

# from image_go import ImageGo

# imagego = ImageGo()

# img = cv2.imread('apple.png')
# lower_reso = cv2.pyrDown(img)
# for i in range(4):
#     lower_reso = cv2.pyrDown(lower_reso)
# 
# imagego.add(img, pos=1, name="apple")
# imagego.add(lower_reso, pos=2, name="lower_reso")
# 
# higher_reso = cv2.pyrUp(img)
# for i in range(2):
#     higher_reso = cv2.pyrUp(higher_reso)
# 
# imagego.add(higher_reso, pos=3, name="higher_reso")
# 
# imagego.show(2, ncol=3, cmap="gray")

if not "test":
    aaa = [
        [[1,1,1], [1,1,1], [1,1,1], [1,1,1]],
        [[1,1,1], [1,1,1], [1,1,1], [1,1,1]],
        [[1,1,1], [1,1,1], [1,1,1], [1,1,1]],
        [[1,1,1], [1,1,1], [1,1,1], [1,1,1]],
        [[1,1,1], [1,1,1], [1,1,1], [1,1,1]],
    ]
    
    bbb = [
        [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
        [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
        [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
        [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
        [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
    ]
    
    aaa = np.array(aaa)
    bbb = np.array(bbb)
    ccc = cv2.subtract(bbb, aaa)
    print(ccc)
    
    ddd = cv2.add(ccc, aaa)
    print(ddd)
    
    ddd2 = cv2.add(aaa, ccc)
    print(ddd2)


if 1:
    A = cv2.imread('apple.png')
    B = cv2.imread('orange.png')
    
    # generate Gaussian pyramid
    G = A.copy()
    gpA = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpA.append(G)
        
    # generate Gaussian pyramid for B
    G = B.copy()
    gpB = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpB.append(G)
    
    # generate Laplacian Pyramid for A
    lpA = [gpA[5]]
    for i in range(5,0,-1):
        GE = cv2.pyrUp(gpA[i])
        gpA_1 = gpA[i-1]
        # TODO shape 总是神奇的不一样....
        L = cv2.subtract(gpA_1, GE)
        lpA.append(L)
    
    # generate Laplacian Pyramid for B
    lpB = [gpB[5]]
    for i in range(5,0,-1):
        GE = cv2.pyrUp(gpB[i])
        # TODO shape 总是神奇的不一样....
        L = cv2.subtract(gpB[i-1],GE)
        lpB.append(L)
    
    # Now add left and right halves of images in each level 
    # numpy.hstack(tup)
    # Take a sequence of arrays and stack them horizontally
    # to make a single array.
    LS = []
    for la,lb in zip(lpA,lpB):
        rows,cols,dpt = la.shape
        ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
        LS.append(ls)
    
    # now reconstruct
    ls_ = LS[0]
    for i in range(1,6):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, LS[i])
    
    # image with direct connecting each half
    real = np.hstack((A[:,:cols/2],B[:,cols/2:]))
    cv2.imwrite('Pyramid_blending2.jpg',ls_)
    cv2.imwrite('Direct_blending.jpg',real)