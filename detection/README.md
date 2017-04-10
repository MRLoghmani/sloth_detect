SLOTH - LABEL PROPAGATION
=========================

>>> Before annotating:

Each sequence of frames needs a different folder and will refer to a different annotation file (.json)
+ Create a new working directory for a sequence of frames
$ cd <this_folder>
$ mkdir <ws_folder_name> && cd <ws_folder_name>

Select the categories you need:
+ Create a proper .txt file containing labels (check example 'categories.txt') in the working dir
$ cd <this-folder>
$ python changecategories.py <label-file-name>

Set up the configurations you need:
+ Copy the folder containing your images in the dir and rename it 'img'
+ Configure the new ws
$ cd ..
$ python setconfig.py <ws_folder_name>

>>> Start annotating:

+ Launch Sloth
$ cd $SLOTH
$ python sloth/bin/sloth --config detection/myconfig.py detection/labels_detection.json

+ Propagate the labels by pressing the Space button




