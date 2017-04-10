'''

changecategories.py
-------------------
Script that modifies 'myconfig.py' file to change the label categories according to the txt file given as argument.
The processed txt file follows the following format:
    - Each line is a new category
    - Each category has a alpha-numeric name (no spaces) and a numeric id
    - At each line name and id are separated by one space

'''

import os.path
import sys


def get_labels(filename):
    """
    Parse the txt category file
    :param filename:    txt category path
    :return labels:     dict where the category name is the key and the id is the value
            classes:    list of all the category names
    """
    labels = {}
    classes = []

    with open(filename) as f:
        for line in f:
            key, value = line.strip().split(' ')
            labels[key.strip()] = value.strip()
            classes.append(key.strip())

    return labels, classes


if len(sys.argv) > 1:
    if sys.argv[1] == '--help':
        print 'Give as argument the name of the txt file containing the considered categories. Default = categories.txt'
        sys.exit(0)
    else:
        categ_file = sys.argv[1]
else:
    categ_file = 'categories.txt'

config_path = 'myconfig.py'

if os.path.isfile(categ_file):
    pattern = 'id'
    config_path = 'myconfig.py'

    content = []
    _, categories = get_labels(categ_file)

    with open(config_path, 'r') as f:
        for line in f:
            if pattern in line:
                line = '\t\t\t\t\t"id": ' + str(categories) + '},\n'
            content.append(line)

    with open(config_path, 'w') as new_file:
        new_file.writelines(content)
else:
    print 'The file <' + categ_file + '> is not in the current folder.'
