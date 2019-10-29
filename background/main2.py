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
        time.sleep(0.001)
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

    #recup main pixel presence
        #except for green pixels (use for our contours)
    for key, value in dico.items():
        if value > max_value and key[0] > 10 and key[1] > 10 and key[2] > 10:
            max_value = value; color = key;

    return color


if __name__ == "__main__":


    path_folder_image = "image_treated/"
    path_image = "image_treated/{}"

    path_folder_image_ok = "image/"
    path_image_ok = "image/{}"

    #img1 = open_picture(path_image_ok.format(liste_image1[i]), 1)


    MM = cv2.ADAPTIVE_THRESH_MEAN_C
    MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    T = cv2.THRESH_BINARY

    R = cv2.RETR_TREE
    P = cv2.CHAIN_APPROX_NONE

    liste_image = os.listdir(path_folder_image)
    liste_image1 = os.listdir(path_folder_image_ok)

    for i in range(len(liste_image)):

        img = open_picture(path_image.format(liste_image[i]), 1)
        height, width, channel = img.shape
        show_picture("img", img, 0, "")

        a = []
        b = []
        c = []

        r = 0
        g = 0
        blue=50
        timmee = 0

        ok = False
        count = 0
        for x in range(0, img.shape[0]):
            for y in range(0, img.shape[1]):
                if img[x, y][0] == 0 and\
                   img[x, y][1] == 0 and\
                   img[x, y][2] == 0:
                   pass
                else:

                    try:
                        if img[x, y][0] > aa + 50 or\
                           img[x, y][0] < aa - 50 or\
                           img[x, y][1] > bb + 50 or\
                           img[x, y][1] < bb - 50 or\
                           img[x, y][2] > cc + 50 or\
                           img[x, y][2] < cc - 50:
                            print("oui")
                            ok = True
                            if timmee == 0 and ok is True:
                                timmee += 1
                        else:
                            ok = False

                    except:
                        pass


                    if timmee == 0:
                        a.append(img[x, y][0])
                        b.append(img[x, y][1])
                        c.append(img[x, y][2])

                    
                    #print(img[x, y])
                    if ok is False:
                        img[x, y] = 255, 0, 0

                    if ok is True:
                        img[x, y] = 0, 0, 255



                    

                    show_picture("img", img, 1, "")



                
            try:
                aa = int(sum(a) / len(a))
                bb = int(sum(b) / len(b))
                cc = int(sum(c) / len(c))
                #print(aa, bb, cc)
            except:
                pass







