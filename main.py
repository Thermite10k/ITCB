from cmath import pi
from PIL import Image
import numpy as np
import sounddevice as sd


image = Image.open("./Static/plane.jpg").convert('L')

# This is the arrya. contains all data
image_array = np.asarray(image, dtype=np.uint8)

Row,Col = image_array.shape #(768, 1024)


# Work on array can be done here


# This is the image back from athe array. np.unit8(I) takes I and
# makes sure that the valuse are [0-255]
#im = image.convert("1")
nullArray = np.zeros((Row,Col), dtype=np.uint8)
for row in range(Row):
    for col in range(Col):
        currentPixel = image_array[row,col]
        estimation  = 0
        if ((image_array[row][col] >= 112 ).any()) :
            estimation = 225
            image_array[row,col] = 225
        else:
            estimation = 0
            image_array[row,col] = 0

        error = currentPixel - estimation

        passRight = error * (0.4375)
        passBottomLeft = error * (0.1875)
        passBottom = error * (0.3125)
        passBottomRight = error * (0.0625) 

        try:
            image_array[row ,   col + 1] += passRight
            image_array[row + 1,col - 1] += passBottomLeft
            image_array[row + 1,col    ] += passBottom
            image_array[row + 1,col + 1] += passBottomRight
        except:
            pass    
        
im = Image.fromarray(np.uint8(image_array))
im.show()

# im = image.convert("1")
# im.show()

#

# np.savetxt("array.txt", bw_array, "%1.00f")
# # im.save('gfg_dum22my_pic.png')
# ================================================================
'''bw_array = np.asarray(im, dtype="int32")
print(bw_array.dtype)
# print(bw_array[0][0])

sound_arr = []
for row in range(Row):
    for col in range(Col):
        if bw_array[row][col] == 1:
            bw_array[row][col] = 1000
        else:
            bw_array[row][col] = 500
        sound_arr.append(bw_array[row][col])'''






# bw_imag_from_array.show()
# ================================================================
