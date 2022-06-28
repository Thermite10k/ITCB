from numba import jit
from PIL import Image
import numpy as np


@jit()
def floydSteinbergDishering(image_array,Row,Col):
    

    
    for row in range(Row):
        for col in range(Col):
            currentPixel = image_array[row,col]
            estimation  = 0
            if ((image_array[row ,col] >= 120 )) :
                estimation = 225
                image_array[row,col] = 225
            else:
                estimation = 0
                image_array[row,col] = 0

            pixelError = currentPixel - estimation

            # passRight = pixelError * (0.4375)
            # passBottomLeft = pixelError * (0.1875)
            # passBottom = pixelError * (0.3125)
            # passBottomRight = pixelError * (0.0625) 

            if(col + 1 < Col):
                image_array[row ,   col + 1] += pixelError * (0.4375)
                if( row + 1 < Row ):
                    image_array[row + 1,col + 1] += pixelError * (0.0625) 
            
            if( row + 1 < Row ):
                image_array[row + 1,col    ] += pixelError * (0.3125)
                if( col - 1 < Col):
                    image_array[row + 1,col - 1] += pixelError * (0.1875)
            
  

            


            # try:
            #     image_array[row ,   col + 1] += passRight
            #     image_array[row + 1,col - 1] += passBottomLeft
            #     image_array[row + 1,col    ] += passBottom
            #     image_array[row + 1,col + 1] += passBottomRight
            # except:
            #     pass    
    return image_array
    

image = Image.open("./Static/final.jpg").convert("L")
image_array = np.asanyarray(image, dtype=np.uint8)
Row,Col = image_array.shape
new_arr = floydSteinbergDishering(image_array,Row,Col)  

im = Image.fromarray(np.bool_(new_arr))
im.show()