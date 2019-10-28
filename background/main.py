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


        #show_picture("blanck", blanck, 0, "")

        gray = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,5)
        th3 = make_line(th3, 10, 255)

        #show_picture("th3", th3, 0, "")


        size = 50
        blanck_th3 = blanck_picture(img)


        for x in range(0, th3.shape[1], size):
            for y in range(0, th3.shape[0], size):

                crop = th3[y:y+50, x:x+50]
                crop = make_line(crop, 2, 255)
                blanck_th = blanck_picture(crop)


                contours, _ = cv2.findContours(crop, R, P)


                for cnt in contours:
                    if cv2.contourArea(cnt) < 1500 and\
                       cv2.contourArea(cnt) > 200:
                        cv2.drawContours(blanck_th,[cnt], -1, (255,255,255), 1)
                        #cv2.fillPoly(blanck_th, pts =[cnt], color=(255, 255, 255))
                        #show_picture("blanck_th", blanck_th, 0, "")

                blanck_th3[y:y+50, x:x+50] = blanck_th

                #show_picture("blanck_th3", blanck_th3, 0, "")


        #show_picture("blanck_th3", blanck_th3, 0, "")

        blanck4 = blanck_picture(blanck_th3)
        gray = cv2.cvtColor(blanck_th3, cv2.COLOR_BGR2GRAY)

        contours, _ = cv2.findContours(gray, R, P)


        for cnts in contours:
            if cv2.contourArea(cnts) > 250:
                #print(cv2.contourArea(cnts))
                cv2.drawContours(blanck4, [cnts], -1, (255,255,255), 1)
                #show_picture("blanck4", blanck4, 0, "")

        #show_picture("blanck4", blanck4, 0, "")



        blanck6 = blanck_picture(img)
        for x in range(0, blanck4.shape[1], size):
            for y in range(0, blanck4.shape[0], size):

                try:
                    crop = blanck4[y:y+50, x:x+50]
                    crop = make_line(crop, 2, 0)
                    gray_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

                    crop1 = blanck4[y-50:y, x-50:x]
                    crop1 = make_line(crop1, 2, 0)
                    gray_crop1 = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)

                    crop2 = blanck4[y+50:y+100, x+50:x+100]
                    crop2 = make_line(crop2, 2, 0)
                    gray_crop2 = cv2.cvtColor(crop2, cv2.COLOR_BGR2GRAY)


                    c = 0; c1 = 0;
                    for x_crop in range(0, crop.shape[1]):
                        for y_crop in range(0, crop.shape[0]):
                            if gray_crop1[x_crop, y_crop] != 0:   
                                c+=1
                            if gray_crop2[x_crop, y_crop] != 0:
                                c1+=1
    

                    if c == 0 and c1 == 0:
                        pass
                    else:
                        blanck6[y:y+size, x:x+size] = crop


                except:
                    pass


        #show_picture("blanck6", blanck6, 0, "")

        gray = cv2.cvtColor(blanck6, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,2)

        contours, _ = cv2.findContours(th3, R, P)

        maxi = 0
        for cnts in contours:
            if cv2.contourArea(cnts) > maxi:
                maxi = cv2.contourArea(cnts)

        blanck7 = blanck_picture(img)
        blanck7 = cv2.cvtColor(blanck7, cv2.COLOR_BGR2GRAY)
        maxi2 = 0
        for cnts in contours:
            if cv2.contourArea(cnts) < maxi and\
             cv2.contourArea(cnts) > maxi2:
                maxi2 = cv2.contourArea(cnts)

        for cnts in contours:
            if cv2.contourArea(cnts) == maxi2:
                x, y, w, h = cv2.boundingRect(cnts)
                blanck7[y:y+h, x:x+w] = 255


        for x in range(0, blanck7.shape[0]):
            for y in range(0, blanck7.shape[1]):
                if blanck7[x, y] == 255:
                    pass
                else:
                    img[x, y] = 0

        show_picture("img", img, 0, "")



















#iscontourconvexe roue





















