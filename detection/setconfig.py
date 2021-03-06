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
        sys.exit('python setconfig.py <arg1> [<arg2>]\narg1: name folder containing the sequence of frames to annotate\narg2: optional argument indicating the name of the folder containing the considered frames [Default = img]')
        sys.exit(0)
    elif len(sys.argv) == 2:
        img_folder_name = 'img'
        sequence_folder = sys.argv[1]
    elif len(sys.argv) == 3:
        img_folder_name = sys.argv[2]
        sequence_folder = sys.argv[1]
else:
    sys.exit('Error: expected at least 1 argument, 0 given. Give --help as argument for furthe information.')

# Managing paths based on current directory
folder_path = os.path.dirname(os.path.realpath(__file__))       # global path: current dir
_, folder_name = os.path.split(folder_path)                     # need to isolate folder name
root_seq_folder, sequence_folder = os.path.split(sequence_folder)
if not sequence_folder:
    _, sequence_folder = os.path.split(root_seq_folder)
#print 'Sequence folder: ', sequence_folder
folder_path = folder_path + '/' + sequence_folder
#print 'Folder path: ', folder_path
labels_path = folder_path + '/labels_' + sequence_folder + '.json'  # path to annotation file
#print 'Labels path: ', labels_path

annotation = []

# The annotation file is initialized only if there is no previous one.
# Delete or move old annotation files to set up a new one
if not os.path.isfile(labels_path):
    cont = container.JsonContainer()
    img_folder_path = folder_path + '/' + img_folder_name + '/*'
    if not os.path.isdir(folder_path + '/' + img_folder_name):
        print folder_path + '/' + img_folder_name
        err_msg = 'Error: no dir named <' + img_folder_name + '> in ' + folder_path
        sys.exit(err_msg)
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
    print 'The file <' + labels_path + '> already exists.\nIf you want to create a new one, please delete of move the file.'
