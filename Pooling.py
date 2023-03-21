import cv2
import numpy as np
import MatplotlibShow

# max pooling (池化)
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


# Read image
img = cv2.imread(r"C:\Users\28692\Documents\Python works\opencv\Figures\lena.png")

# Max pooling
out = max_pooling(img)

#Print 2 images
MatplotlibShow.ImgShow2(img,out)


# # Save result
# cv2.imwrite("out.jpg", out)
# cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

