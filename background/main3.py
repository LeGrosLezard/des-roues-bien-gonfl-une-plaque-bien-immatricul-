import os
import cv2
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2\main")

import imutils
import numpy as np
import time
import matplotlib.pyplot as plt
from PIL import Image




def open_picture(image, mode):
    """We open picture"""
    if mode == 1:
        img = cv2.imread(image)
    elif mode == 0:
        img = cv2.imread(image, 0)
    return img

def show_picture(name, image, mode, destroy):
    """Show picture"""
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if mode == 1:
        time.sleep(0.000000000000001)
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


def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)


def main_color_background(img):
    """
        Here we recup the main color
        by the recurrent pixel
    """

    dico = {}; max_value = 0; color = []

    #Convert picture to array
    im = Image.fromarray(img)
    #data from array recup value pixels 
    for value in im.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1
    return dico




MM = cv2.ADAPTIVE_THRESH_MEAN_C
MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
T = cv2.THRESH_BINARY

R = cv2.RETR_EXTERNAL
P = cv2.CHAIN_APPROX_NONE


if __name__ == "__main__":


    path_folder_image = "image/"
    path_image = "image/{}"
    liste_image = os.listdir(path_folder_image)





    size = 10
    for i in range(len(liste_image)):

        img = open_picture(path_image.format(liste_image[i]), 1)
        show_picture("img", img, 0, "")


        for nb in range(1, 4):
            #court image
            for x in range(0, img.shape[1], size*nb):
                for y in range(0, img.shape[0], size*nb):
                    a = 0; b = 0; c = 0; d = 0;

                    #5 par 5
                    crop_in = img[y:y+size*nb, x:x+size*nb]
                    #show_picture("crop_in", crop_in, 0, "")
                    for i in crop_in.tolist():
                        for j in i:

                            #moyenne
                            a += j[0]; b+=j[1];c+=j[2]
                            d+=1

                    if d != 0:

                        #reatribut couleur
                        img[y:y+size*nb, x:x+size*nb] = int(a/d), int(b/d), int(c/d)
                        #show_picture("img", img, 0, "")

            show_picture("imgpix", img, 0, "")




























                












