import os
import cv2
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2\main")

import imutils
import numpy as np
import time
import matplotlib.pyplot as plt
from PIL import Image

import cv2
import numpy as np
from matplotlib import pyplot as plt


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


    for key, value in dico.items():
        if value > max_value and key != (0):
            max_value = value; color = key;


    return dico, color



def rotation(img, degrees):
    """
        Rotation of the picture via his center
    """
    
    rows = img.shape[0]
    cols = img.shape[1]

    img_center = (cols / 2, rows / 2)
    M = cv2.getRotationMatrix2D(img_center, degrees, 1)

    #Rotate picture with white border
    rotated = cv2.warpAffine(img, M, (cols, rows), borderValue=(0,0,0))
    #show_picture("rotated", rotated, 0, "y")

    return rotated


MM = cv2.ADAPTIVE_THRESH_MEAN_C
MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
T = cv2.THRESH_BINARY

R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE


if __name__ == "__main__":


    path_folder_image = "image/"
    path_image = "image/{}"
    liste_image = os.listdir(path_folder_image)





    size = 5
    for i in range(len(liste_image)):

        img = open_picture(path_image.format(liste_image[i]), 1)




        height, width, channel = img.shape
        add_w = width % 10
        add_h = height % 10

        img = cv2.resize(img, (300, 300))
        height, width, channel = img.shape

        #show_picture("img", img, 0, "")

        
        copy = img.copy()
        ccopy = img.copy()
        ccopsy = img.copy()
        yaya = img.copy()
        cocopy = img.copy()

        dzadazda= img.copy()

























        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        rectangle = (20, 20, 50+width-100, 50+height-80)



        mask = np.zeros(image_rgb.shape[:2], np.uint8)


    

        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)


        cv2.grabCut(image_rgb, # Our image
                    mask, # The Mask
                    rectangle, # Our rectangle
                    bgdModel, # Temporary array for background
                    fgdModel, # Temporary array for background
                    10, # Number of iterations
                    cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

        # Create mask where sure and likely backgrounds set to 0, otherwise 1
        mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')


        image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]




























        gray = cv2.cvtColor(image_rgb_nobg, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,1)
        contours, _ = cv2.findContours(th3, R, P)


        blanck = blanck_picture(img);

        maxi = 0
        maxi1 = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > maxi:
                maxi = cv2.contourArea(cnt)
            if cv2.contourArea(cnt) < maxi and\
               cv2.contourArea(cnt) > maxi1:
                maxi1 = cv2.contourArea(cnt)


        for cnts in contours:
            if cv2.contourArea(cnts) == maxi1:
                cv2.drawContours(blanck,[cnts],-1,(255,255,255), 1)
                cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))

                #show_picture("blanck", blanck, 0, "")

        #show_picture("blanck", blanck, 0, "")


        kernel = np.ones((4,4),np.uint8)
        blanck111 = cv2.erode(blanck,kernel,iterations = 1)

        #show_picture("blanck", blanck, 0, "")

        blanck111 = cv2.morphologyEx(blanck111, cv2.MORPH_OPEN, kernel)



        blanck111 = cv2.cvtColor(blanck111, cv2.COLOR_BGR2GRAY)

        aa = blanck111.copy()




        for x in range(0, blanck111.shape[0]):
            for y in range(0, blanck111.shape[1]):
                if blanck111[x,y] == 255:
                    pass
                else:
                    ccopsy[x,y] = 0


        #show_picture("ccopsy", ccopsy, 0, "")



    





        kernel = np.ones((2,2),np.uint8)
        aa = cv2.erode(aa,kernel,iterations = 1)


        #show_picture("blanck111", blanck111, 0, "")

 

        for x in range(0, aa.shape[0]):
            for y in range(0, aa.shape[1]):
                if aa[x,y] == 255:
                    pass
                else:
                    ccopsy[x,y] = 0


        #show_picture("zadza", ccopsy, 0, "")










        gray = cv2.cvtColor(ccopsy, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,5)



        maxi = 0
        maxi1 = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > maxi:
                maxi = cv2.contourArea(cnt)
            if cv2.contourArea(cnt) < maxi and\
               cv2.contourArea(cnt) > maxi1:
                maxi1 = cv2.contourArea(cnt)

                

        blanck2 = blanck_picture(img);
        blanck2 = cv2.cvtColor(blanck2, cv2.COLOR_BGR2GRAY)


        for cnts in contours:
            if cv2.contourArea(cnts) == maxi or\
               cv2.contourArea(cnts) == maxi1:
                #print(cv2.contourArea(cnts))
                cv2.drawContours(blanck2,[cnts],-1,(255,255,255), 10)
                #cv2.fillPoly(blanck2, pts =[cnts], color=(255, 255, 255))



        #show_picture("blanck2", blanck2, 0, "")


        kernel = np.ones((1,1),np.uint8)
        blanck2 = cv2.erode(blanck2,kernel,iterations = 1)

        #show_picture("vcxv", blanck2, 0, "")

        for x in range(0, blanck2.shape[0]):
            for y in range(0, blanck2.shape[1]):
                if blanck2[x, y] == 255:
                    ccopsy[x,y] = 0, 0, 0


        show_picture("zadza", ccopsy, 0, "")









        
