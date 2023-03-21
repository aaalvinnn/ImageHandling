import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#imread()的第二个参数取1,0,-1 代表彩色，灰色，包括alpha通道(透明度)
img1 = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\figure1.jpg',1)

#将cv2的BGR通道转换为RGB通道
def Transform_BGR(img1):
    # 判断是否为三通道
    if(len(img1.shape)==3):
        b,g,r = cv.split(img1)
        img2 = cv.merge([r,g,b])
        return img2
    else:
        print('不是三通道彩色图')
#对比显示两个图像,便于其他文件使用，此处封装为函数
def ImgShow2(img1,img2):
    #定义plt读取色彩模式,若为单通道图，则gray
    colour = 'gray'
    #若读取的是彩色三通道（因为有些地方只能用灰色单通道图
    if(len(img1.shape)==3 and img1.shape[2]==3):
        img1 = Transform_BGR(img1)
        img2 = Transform_BGR(img2)
        colour = None
    #plt 输出图像
    #作:处理前,仍为BGR通道
    plt.subplot(121)
    plt.imshow(img1, cmap=colour,interpolation = 'bicubic') #双三次插值,放大图像像素点的个数
    plt.xticks([]), plt.yticks([]) # 隐藏 x 轴和 y 轴上的刻度值
    plt.title('old')
    # 处理后,RGB通道
    plt.subplot(122)
    plt.imshow(img2,cmap=colour,interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([]) # 隐藏 x 轴和 y 轴上的刻度值
    plt.title('new')
    plt.show()

# img2 = Transform_BGR(img1)
# ImgShow2(img1,img2)

# cv2打印图像
# cv.imshow('bgr image',img) # expects true color
# cv.imshow('rgb image',img2) # expects distorted color
# cv.waitKey(0)
# cv.destroyAllWindows()
