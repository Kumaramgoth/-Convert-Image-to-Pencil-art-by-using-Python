import numpy as np
import imageio.v2 as imageio
import scipy.ndimage
import cv2

img = "pk.jpeg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

def dodge(front, back):
    final_sketch = front*225 /(225-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back == 255] = 255

    return final_sketch.astype('uint8')


ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 255-gray

blur = scipy.ndimage.filters.gaussian_filter(i, sigma =15)

r = dodge(blur, gray) #this function will convert our image to skech by taking the parameter as blur and gray.

cv2.imwrite('pk_sketch.png',r)







