import os
import cv2
import numpy as np
import cv2
from matplotlib import pyplot as plt

from PIL import Image



def open_picture(image, mode):
    """We open picture"""
    if mode == 1:
        img = cv2.imread(image)
    if mode == 0:
        img = cv2.imread(image, 0)
    return img


def show_picture(name, image, mode, destroy):
    """Show picture"""
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if mode == 1:
        time.sleep(1)
        cv2.destroyAllWindows()
    if destroy == "y":
        cv2.destroyAllWindows()

def blanck_picture(img):
    """ Create a black picture"""
    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0
    return blank_image



def meanning(img):


    size = 2
    nb = 1


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


    
    show_picture("imgpix", img, 0, "")

    return img







def to_up(number):

    #the rest of division
    many = number % 50

    if many < 50:
        number = number - many
    else:
        to_ten = 50 - many
        number = number + to_ten


    return number






def make_mean(img):

    #1 hog ex pas mélanger nimporte quoi

    neightboors = 3

    
    for x in range(0, img.shape[1], neightboors):
        for y in range(0, img.shape[0], neightboors):
            r = 0; g = 0; b = 0; counter = 0;
            for i in img[y:y+neightboors, x:x+neightboors].tolist():
                for j in i:
                    r += j[0]
                    g += j[1]
                    b += j[2]
                    counter += 1

            if counter > 0:
                color = int(r/counter), int(g/counter), int(b/counter)
                img[y:y+neightboors, x:x+neightboors] = color
    return img
 




def put_color(blanck):


    color_dico = {}

    blanck = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)
    for x in range(0, blanck.shape[0]):
        for y in range(0, blanck.shape[1]):
            color_dico[blanck[x, y]] = 0

    print(color_dico)



    blanck2 = blanck_picture(blanck);
    for x in range(0, blanck.shape[0]):
        for y in range(0, blanck.shape[1]):

            if blanck[x,y] >= 200:
                blanck2[x,y] = 255, 255, 255

            elif blanck[x,y] < 200 and blanck[x,y] >= 150:
                blanck2[x,y] = 255, 0, 0

            elif blanck[x,y] > 150 and blanck[x,y] >= 100:
                blanck2[x,y] = 0, 255, 255


            elif blanck[x,y] < 100 and blanck[x,y] >= 50:
                blanck2[x,y] = 0, 255, 0

            elif blanck[x,y] >= 0 and blanck[x,y] < 50:
                blanck2[x,y] = 0, 0, 0


    return blanck2






def color_value(img):


    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    liste_image = []

    copy = img.copy();blanck = blanck_picture(img);
    for x in range(0, gray.shape[0]):
        for y in range(0, gray.shape[1]):


            number = to_up(gray[x,y])
            #print(number)

            blanck[x,y] = number

            copy[x,y] = 255, 100, 100

    return blanck








if __name__ == "__main__":


    path_folder_image = "image/"
    path_image = "image/{}"
    liste_image = os.listdir(path_folder_image)



    for i in range(len(liste_image)):

        img0 = open_picture(path_image.format(liste_image[i]), 1)
        show_picture("img0", img0, 0, "")

        img = color_value(img0)
        show_picture("img1", img, 0, "")

        img2 = put_color(img)
        show_picture("img2", img2, 0, "")


        img_pix = meanning(img)
        show_picture("img_pix", img_pix, 0, "")


        img_pix = put_color(img_pix)
        show_picture("img_pix2", img_pix, 0, "")




        























