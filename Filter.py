import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import MatplotlibShow
img = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\lena.png',1)
img = MatplotlibShow.Transform_BGR(img)

# 1.二维卷积（图像滤波）(相当于手搓均值滤波)
def ImageKernel_example(img):
    kernel = np.ones((20,20),np.float32)/400
    dst = cv.filter2D(img,-1,kernel)    #-1为ddepth期望深度，-1表示输出类型和输入相同
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()
# ImageKernel_example(img)

# 2.均值滤波
def MeanFilter_example(img):
    blur = cv.blur(img,(20,20))
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()
# MeanFilter_example(img)

# 3.高斯滤波
def GaussianFilter_example(img):
    blur = cv.GaussianBlur(img,(21,21),0)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()
# GaussianFilter_example(img)

# 4.中值滤波
def MedianFilter_example(img):
    blur = cv.medianBlur(img,21)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()
# MedianFilter_example(img)

# 5.双边滤波
def BilateralFilter_example(img):
    blur = cv.bilateralFilter(img,9,75,75)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()   
# BilateralFilter_example(img)

# 6.池化（下采样）# max pooling (池化)
def max_pooling(img, grid=8):
    # Max Pooling
    out = img.copy()

    H, W, C = img.shape
    Nh = int(H / grid)
    Nw = int(W / grid)

    for y in range(Nh):
        for x in range(Nw):
            for c in range(C):
                out[grid*y:grid*(y+1), grid*x:grid*(x+1), c] = np.max(out[grid*y:grid*(y+1), grid*x:grid*(x+1), c])

    return out
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(max_pooling(img)),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()   
