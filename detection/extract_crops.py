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

    for f in frames:
        img_name = f["filename"]
        img = cv2.imread(DIR + '/' + img_name)
        print DIR + img_name
        crop_path = DIR + '/crop/' + img_name
        if not os.path.exists(crop_path):
            os.makedirs(crop_path)
        for num, a in enumerate(f["annotations"]):
            x = int(round(a["x"]))
            y = int(round(a["y"]))
            delta_y = int(round(a["height"]))
            delta_x = int(round(a["width"]))
            crop = img[y:y+delta_y, x:x+delta_x, :]
            plt.imshow(crop)
            plt.show()

            cv2.imwrite(crop_path + '/' + a["id"] + '_' + str(num), crop)

