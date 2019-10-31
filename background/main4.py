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


    neightboors = 10
    operate = 1


    #court image
    for x in range(0, img.shape[1], 1):
        for y in range(0, img.shape[0], neightboors*operate):
            a = 0; b = 0; c = 0; d = 0;

            #5 par 5
            crop_in = img[y:y+neightboors*operate, x]
            #show_picture("crop_in", crop_in, 0, "")
            for i in crop_in.tolist():
                for j in i:

                    #moyenne
                    a += j
                    d+=1

            if d != 0:

                #reatribut couleur
                img[y:y+neightboors*operate, x] = int(a/d)


    return img




def make_mean(img):

    #1 hog ex pas mélanger nimporte quoi

    neightboors = 3

    
    for x in range(0, img.shape[1], neightboors):
        for y in range(0, img.shape[0], 1):
            r = 0; g = 0; b = 0; counter = 0;
            for i in img[y, x:x+neightboors].tolist():
                r += i[0]
                g += i[1]
                b += i[2]
                counter += 1

            if counter > 0:
                color = int(r/counter), int(g/counter), int(b/counter)
                img[y, x:x+neightboors] = color


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
                blanck2[x,y] = 0, 0, 255


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





def mask(img):


    def colors(img, x, y, c1, c2, c3, blanck):
        if img[x,y][0] == c1 and\
            img[x,y][1] == c2 and\
            img[x,y][2] == c3:
                blanck[x, y] = 255, 255, 255
        return blanck


    blanck_blue = blanck_picture(img);
    blanck_black = blanck_picture(img);
    blanck_red = blanck_picture(img);
    blanck_green = blanck_picture(img);
    blanck_white = blanck_picture(img);
    
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):

            blue = colors(img, x, y, 255, 0, 0, blanck_blue)
            red = colors(img, x, y, 0, 0, 255, blanck_red)
            green = colors(img, x, y, 0, 255, 0, blanck_green)
            white = colors(img, x, y, 255, 255, 255, blanck_white)
            black = colors(img, x, y, 0, 0, 0, blanck_black)
            
            
    show_picture("blue", blue, 0, "")
    show_picture("red", red, 0, "")
    show_picture("green", green, 0, "")
    show_picture("white", white, 0, "")
    show_picture("black", black, 0, "")

            

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
        if value > max_value and key != (0, 255, 0):
            max_value = value; color = key;

    return color



def make_area(img):


    t = 0
    val = ()
    counter = 0
    activate = False

    copy = img.copy()
    size = 1


    for x in range(0, img.shape[1], size):
        for y in range(0, img.shape[0], size):

            try:
                crop = img[y-size:y+size, x-size:x+size]


                color = main_color_background(crop)
                #print(color)


                copy[y-size:y+size, x-size:x+size] = color

                #show_picture("crop", crop, 0, "")
                #show_picture("copy", copy, 1, "")
            except:
                pass

    return copy








def contours():
    pass

def bounding():
    pass


MM = cv2.ADAPTIVE_THRESH_MEAN_C
MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
T = cv2.THRESH_BINARY

R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE


if __name__ == "__main__":


    #faire plusieurs truck
    #1truk cuillere
    #ce truk


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


        img3 = make_area(img2)
        show_picture("img3", img3, 0, "")





        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,5)
        contours, _ = cv2.findContours(th3, R, P)
        
        blanck2_test = blanck_picture(img);


        maxi = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > maxi:
                maxi = cv2.contourArea(cnt)


        for cnts in contours:
            if cv2.contourArea(cnts) != maxi and cv2.contourArea(cnts) < 300:
                print(cv2.contourArea(cnts))
                #cv2.drawContours(blanck2_test,[cnts],-1,(255,255,255), 1)
                cv2.fillPoly(blanck2_test, pts =[cnts], color=(255, 255, 255))



                show_picture("blanck2_test", blanck2_test, 0, "")


















