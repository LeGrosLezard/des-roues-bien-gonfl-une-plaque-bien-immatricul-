import os
import cv2
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2\main")

import imutils
import numpy as np
import time


path_folder_image = "image_treated/"
path_image = "image_treated/{}"

def open_picture(image):
    """We open picture"""
    img = cv2.imread(image)
    return img

def show_picture(name, image, mode, destroy):
    """Show picture"""
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if mode == 1:
        time.sleep(0.1)
        #cv2.destroyAllWindows()
    if destroy == "y":
        cv2.destroyAllWindows()

def save_picture(name, picture):
    """saving picture"""
    cv2.imwrite(name, picture)

def blanck_picture(img):
    """ Create a black picture"""
    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0
    return blank_image




if __name__ == "__main__":


    liste_image = os.listdir(path_folder_image)

    for i in liste_image:

        img = open_picture(path_image.format(i))


        c = 300
        for i in range(400):
            copy = img.copy()
            cv2.circle(copy, (int(copy.shape[1]/2), int(copy.shape[0]/2)), c, (0,0,255), 5)
            c -= 1





            show_picture("copy", copy, 1, "")


















