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

if __name__ == "__main__":


    path_folder_image = "image/"
    path_image = "image/{}"



    liste_image = os.listdir(path_folder_image)


    for i in range(len(liste_image)):

        img = open_picture(path_image.format(liste_image[i]), 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        show_picture("gray", gray, 0, "")


        dico1 = {}
        dico = main_color_background(gray)
        for key, value in dico.items():
            dico1[key] = []

        v = 0

        r = 0
        g = 0
        b = 0

        bb = False
        gg = False
        t = 0

        r_no = False
        b_no = False
        g_no = False
        for key, value in dico1.items():
            no = False
            if key < v + 5 and key > v - 5:
                no = True

            v = key

            value.append([b, g, r])




            if no is True:
                pass




            else:
                if r < 240:
                    r += 20
  
                if r >= 240 and b <= 240:
                    b += 20

                if b >= 240:
                    g += 20

                if g >= 240:
                    r = 0
                    b = 0
                    g = 0


        t += 1
        print(dico1)


        
        for x in range(0, gray.shape[0]):
            for y in range(0, gray.shape[1]):
                for key, value in dico1.items():
                    if gray[x, y] == key:
                        img[x, y] = value[0][0], value[0][1], value[0][2]


                        show_picture("img", img, 0, "")






























                












