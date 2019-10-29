import os
import cv2
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2\main")

import imutils
import numpy as np






path_folder_image = "image/"
path_image = "image/{}"

def open_picture(image):
    """We open picture"""
    img = cv2.imread(image)
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

def save_picture(name, picture):
    """saving picture"""
    cv2.imwrite(name, picture)

def blanck_picture(img):
    """ Create a black picture"""
    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0
    return blank_image




def make_line(thresh, size, color):
    """We make line for detect more than one area
    with border, on eyelashes is paste to the border"""

    cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (color), size)
    cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (color), size)
    cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (color), size)
    cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (color), size)

    return thresh



def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)



if __name__ == "__main__":

    cc = 0
    MM = cv2.ADAPTIVE_THRESH_MEAN_C
    MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    T = cv2.THRESH_BINARY

    R = cv2.RETR_TREE
    P = cv2.CHAIN_APPROX_NONE
    liste_image = os.listdir(path_folder_image)

    for i in liste_image:

        img = open_picture(path_image.format(i))
        height, width, channel = img.shape
        add_w = width % 10
        add_h = height % 10

        img = cv2.resize(img, (width*2 + add_w, height*2 + add_h))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        size = 100;
        blanck1 = blanck_picture(img);
        bloc = 1
        for x in range(0, gray.shape[1], size):
            for y in range(0, gray.shape[0], size):

                crop = gray[y:y+size, x:x+size]

                blanck = blanck_picture(crop); 
                th3 = cv2.adaptiveThreshold(crop, 255, MG, T,11,5)

                contours, _ = cv2.findContours(th3, R, P)
                for cnts in contours:
                    if cv2.contourArea(cnts) > 100:
                        #print(cv2.contourArea(cnts))
                        cv2.drawContours(blanck, [cnts], -1, (0,255,0), 1)

                        #show_picture("blanck", blanck, 0, "")

                        blanck = make_line(blanck, 5, 0)
                        blanck1[y:y+size, x:x+size] = blanck


                


            bloc += 5
        show_picture("blanck1", blanck1, 0, "")










