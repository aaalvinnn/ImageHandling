import numpy as np
import cv2 as cv
import MatplotlibShow
import matplotlib.pyplot as plt
img = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\figure1.jpg',1)
# 1.缩放
def ImageResize(img,fx=2,fy=2):
    # way1 fx和fx分别代表横纵坐标的大小
    res = cv.resize(img,None,fx=fx, fy=fy, interpolation = cv.INTER_CUBIC)
    # # way2
    # height, width = img.shape[:2]
    # res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
    return res

# 2.平移(剩下的区域用黑色来填充)
# 注意，因warpAffine函数只能对灰度图做处理，所以传入的img需为灰度图（通道数为1）
def ImageTranslation(img,x=10,y=5):
    img_temp = img
    rows,cols = img_temp.shape
    M = np.float32([[1,0,x],[0,1,y]])
    dst = cv.warpAffine(img_temp,M,(cols,rows))
    return dst

# 3.旋转 （逆时针旋转。不放大图形）
# 该函数也只能对单一通道（灰色图）做变换
def ImageRotate(img,theta=90):
    rows,cols = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),theta,1)
    dst = cv.warpAffine(img,M,(cols,rows))
    return dst

# 4.仿射 
def ImageAffine(img, *pst1, **pst2):
    rows,cols,ch = img.shape
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv.getAffineTransform(pts1,pts2)
    dst = cv.warpAffine(img,M,(cols,rows))
    return dst

# 5.透视
def ImagePerspective(img):
    rows,cols,ch = img.shape
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(300,300))
    return dst


MatplotlibShow.ImgShow2(img,ImagePerspective(img))
