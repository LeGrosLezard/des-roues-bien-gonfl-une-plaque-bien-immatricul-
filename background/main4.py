import os
import cv2
import numpy as np
import cv2
from matplotlib import pyplot as plt





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


def to_up(number):

    #the rest of division
    many = number % 100


    if many < 50:
        number = number - many
    else:
        to_ten = 100 - many
        number = number + to_ten


    return number


    

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

    show_picture("copy", copy, 0, "")
    show_picture("blanck", blanck, 0, "")
















if __name__ == "__main__":


    path_folder_image = "image/"
    path_image = "image/{}"
    liste_image = os.listdir(path_folder_image)



    for i in range(len(liste_image)):

        img = open_picture(path_image.format(liste_image[i]), 1)


        color_value(img)







        























