from skimage import io, img_as_float , color
import matplotlib.pyplot as plt
import numpy as np
import os

folder_name="image"
drive_path="C:"
file_list=os.listdir(drive_path+"/{}".format(folder_name))

for index,file_name in enumerate(file_list):    
    if file_name.__contains__(".jpg"):
        image = img_as_float(io.imread("{}/{}/{}".format(drive_path,folder_name,file_name)))        
        # Select all pixels almost equal to white
        # (almost, because there are some edge effects in jpegs
        # so the boundaries may not be exactly white)
        white = np.array([1, 1, 1])
        mask = np.abs(image - white).sum(axis=2) < 0.5

        # Find the bounding box of those pixels
        coords = np.array(np.nonzero(~mask))
        top_left = np.min(coords, axis=1)
        bottom_right = np.max(coords, axis=1)

        out = image[top_left[0]:bottom_right[0],
                    top_left[1]:bottom_right[1]]


        io.imsave(drive_path+"/"+folder_name+"/"+file_name, out)
        print("%s. %s" % (index+1, file_name))
print('\n','finish')    
    # plt.imshow(out)
    # plt.show()
