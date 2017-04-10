'''
setconfig.py
------------
Configuration set up to create the annotation file (.json) for the indicated folder.
Requires as argument the name of the folder where the target images are stored. If empty, default name 'img' is
considered.
Comment: there might be a better way to do it by using Sloths built-in func
'''

import os.path
import glob
import sys
from sloth.annotations import container

if len(sys.argv) > 1:
    if sys.argv[1] == '--help':
        print 'Give as argument the name of the folder containing the unlabelled images. Default = img'
        sys.exit(0)
    else:
        img_folder_name = sys.argv[1]
else:
    img_folder_name = 'img'

# Managing paths based on current directory
folder_path = os.path.dirname(os.path.realpath(__file__))       # global path: current dir
_, folder_name = os.path.split(folder_path)                     # need to isolate folder name
labels_path = folder_path + '/labels_' + folder_name + '.json'  # path to annotation file

annotation = []

# The annotation file is initialized only if there is no previous one.
# Delete or move old annotation files to set up a new one
if not os.path.isfile(labels_path):
    cont = container.JsonContainer()
    img_folder_path = folder_path + '/' + img_folder_name + '/*'
    img_path = [img for img in glob.glob(img_folder_path)]  # acquire all image paths
    img_path.sort()
    for i in img_path:
        _, filename = os.path.split(i)
        label = dict()
        label['class'] = 'image'
        label['filename'] = img_folder_name + '/' + filename
        annotation.append(label)

    cont.serializeToFile(labels_path, annotation)
else:
    print 'The file <' + labels_path + \
          '> already exists.\nIf you want to create a new one, please delete of move the file.'
