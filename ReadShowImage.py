import numpy as np
import cv2 as cv
#imread()的第二个参数取1,0,-1 代表彩色，灰色，包括alpha通道(透明度)
img = cv.imread(r'C:\Users\28692\Documents\Python works\opencv\Figures\figure1.jpg',1)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if k == 27: # 等待ESC退出
 cv.destroyAllWindows()
elif k == ord('s'): # 等待关键字，保存和退出
 cv.imwrite('messigray.png',img)
 cv.destroyAllWindows()
