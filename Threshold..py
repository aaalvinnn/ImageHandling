"""
图像的二值化或阈值化 (Binarization) 旨在提取图像中的目标物体，
将背景以及噪声区分开来。通常会设定一个阈值，通过阈值 将图像的像素
划分为两类：大于阈值的像素群和小于阈值的像素群。灰度转换处理后的图像中，
每个像素都只有一个灰度值，其大小表示明暗程度。二值化处理可以将图像中的
像素划分为两类颜色。
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import MatplotlibShow

# 1.简单阈值法 threshold()
def Threshold_example():
    #用单通道的图来操作
    img = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\Threshold.png',0)
    if(len(img.shape)==3):
        img = MatplotlibShow.Transform_BGR(img)
    #ret是返回值,thresh1是返回的图像
    thresh = 127    #阈值
    ret,thresh1 = cv.threshold(img,thresh,255,cv.THRESH_BINARY)    #低于阈值：0；高于阈值：255
    ret,thresh2 = cv.threshold(img,thresh,255,cv.THRESH_BINARY_INV)    #低于阈值：255；高于阈值：0
    ret,thresh3 = cv.threshold(img,thresh,255,cv.THRESH_TRUNC) #低于阈值：不变；高于阈值：阈值
    ret,thresh4 = cv.threshold(img,thresh,255,cv.THRESH_TOZERO)    #低于阈值：0；高于阈值：不变
    ret,thresh5 = cv.threshold(img,thresh,255,cv.THRESH_TOZERO_INV)    #低于阈值：不变；高于阈值：0
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
# Threshold_example()

# 2.自适应阈值法 
# 适用于获取的图像明暗不均匀
def AdaptiveThreshold_example():
    img = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\AdaptiveThreshold.png',0)
    img = cv.medianBlur(img,5)
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,11,2)
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
# AdaptiveThreshold_example()

# 3.Otsu二值化
# 通过算法找到阈值，适用于噪声图像(大部分二值化场合都可用该方法)
def OtsuThreshold_example():
    img = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\noisy2.png',0)
    # 全局阈值
    ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    # Otsu 阈值
    ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # 经过高斯滤波的 Otsu 阈值
    blur = cv.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # 画出所有的图像和他们的直方图
    images = [img, 0, th1,
            img, 0, th2,
            blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
            'Original Noisy Image','Histogram',"Otsu's Thresholding",
            'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()
OtsuThreshold_example()