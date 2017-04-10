'''

suggestlabel.py
---------------
Propagate the labels of the previous image to the current one. Use <templatematching.py> to determine corrections between the adjacent frames.

'''


import os
import sys
import glob
import copy
import subprocess
from sloth.annotations import container
from templatematching import annotationAdjustment

try:
    sloth_path = os.environ['SLOTH']
except:
    sys.exit('Error: env var SLOTH missing.')

## TODO: get folder path from external argument
script_path = sloth_path + '/detection/suggestlabels.py'
folder_path, _ = os.path.split(script_path)
#labels_path = folder_path + '/*.json'
labels_path = sloth_path + '/' + sys.argv[2]
all_jsons = [file_path for file_path in glob.glob(labels_path)]

if len(all_jsons) < 1:
    sys.exit('Error: annotation .json file missing. Please launch <setconfig.py> for creating one')
elif len(all_jsons) == 1:
    # Read and parse annotation file
    _, img_name = os.path.split(sys.argv[1])
    img_num = int(img_name[:-4])
    print img_num
    cont = container.JsonContainer()
    labels_path = all_jsons[0]
    ann = cont.parseFromFile(labels_path)
    dic1 = copy.deepcopy(ann[img_num - 2])
    print 'New annotations before processing: ', dic1
    print ann[img_num - 2]["filename"]
    dic1['filename'] = sys.argv[1]
    print dic1['filename']
    
    # Propagate all the labels in <img_name> to the next image
    for a in dic1["annotations"]:
        rect = [a["x"],a["y"],a["height"],a["width"]]
        ref_img_name = '/img/' + '%03d.jpg' %(img_num - 1)
        target_img_name = '/img/' + '%03d.jpg' %img_num

        top_left = annotationAdjustment( rect, ref_img_name, target_img_name)
        a["x"] = top_left[0]
        a["y"] = top_left[1]		

    print 'New final annotation ', dic1["annotations"][0]

    ann[img_num - 1] = copy.deepcopy(dic1)

    cont.serializeToFile(labels_path, ann)
else:
    sys.exit('Error: more than one annotation .json file found. Please make sure the annotation file is unique.')

