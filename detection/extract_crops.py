import os
import sys
import cv2
import glob
import copy
import subprocess
from sloth.annotations import container
from matplotlib import pyplot as plt

if len(sys.argv) < 2:
    sys.exit('Error: 3 args expected; specify .json annotation file and image folder.')
else:
    DIR = os.path.dirname(os.path.abspath(__file__))
    label_path = DIR + '/' + sys.argv[1]
    print label_path
    cont = container.JsonContainer()
    frames = cont.parseFromFile(label_path)

    crop_num = 0

    for f in frames:
        img_name = f["filename"]
        img = cv2.imread(DIR + '/' + img_name)
        print DIR + '/' + img_name
        crop_path = DIR + '/crop/' + img_name
        plt.imshow(img)
        #plt.show()

        for a in f["annotations"]:
            print '*************', img_name, a["id"]
            categ = a["id"]
            categ_path = DIR + '/crop/' + categ
            if not os.path.exists(categ_path):
                os.makedirs(categ_path)
            x = int(round(a["x"]))
            y = int(round(a["y"]))
            delta_y = int(round(a["height"]))
            delta_x = int(round(a["width"]))
            crop = img[y:y+delta_y, x:x+delta_x, :]
            #plt.imshow(crop)
            #plt.show()

            crop_num += 1

            cv2.imwrite(categ_path + '/' + str(crop_num) + '.png', crop)

