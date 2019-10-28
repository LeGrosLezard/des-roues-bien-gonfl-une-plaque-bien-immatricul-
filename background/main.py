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
        blanck = blanck_picture(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 3)
        th2 = cv2.adaptiveThreshold(blur,255, MM, T , 11, 10)

        contours, _ = cv2.findContours(th2, R, P)
        for cnts in contours:
            cv2.drawContours(blanck, [cnts], -1, (0,255,0), 1)


        show_picture("blanck", blanck, 0, "")

        gray = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,5)
        th3 = make_line(th3, 10, 255)

        show_picture("th3", th3, 0, "")


        maxi = 0
        maxi1 = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > maxi:
                maxi = cv2.contourArea(cnt)
                print(maxi)
            
        blanck5 = blanck_picture(img)
        contours, _ = cv2.findContours(th3, R, P)
        for cnt in contours:
            if cv2.contourArea(cnt) < 145272 and\
               cv2.contourArea(cnt) > 1000:
                #print(cv2.contourArea(cnt))
                cv2.fillPoly(blanck5, pts =[cnt], color=(255, 255, 255))
        show_picture("blanck5", blanck5, 0, "")


        for x in range(0, blanck5.shape[0]):
            for y in range(0, blanck5.shape[1]):
                if blanck5[x, y][0] == 255 and\
                   blanck5[x, y][1] == 255 and\
                   blanck5[x, y][2] == 255:
                    pass
                else:
                    img[x, y] = 255, 26, 100

        show_picture("img", img, 0, "")










