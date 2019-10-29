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
        blanck = blanck_picture(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        th2 = cv2.adaptiveThreshold(blur, 255, MM, T , 11, 2)

        show_picture("th2", th2, 0, "")


        blanck = blanck_picture(img)
        gray = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)

        contours, _ = cv2.findContours(th2, R, P)


        maxi = 0
        for cnts in contours:
            if cv2.contourArea(cnts) > maxi:
                maxi = cv2.contourArea(cnts)

        copy = img.copy()
        for cnts in contours:
            if cv2.contourArea(cnts) != maxi and\
               cv2.contourArea(cnts) > 1000:
                print(cv2.contourArea(cnts))
                cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
                (x, y, w, h) = cv2.boundingRect(cnts)
                cv2.rectangle(copy, (x, y), (x+w, y+h), (0, 0, 255), 5)
        show_picture("th2", blanck, 0, "")
        show_picture("copy", copy, 0, "")
        





