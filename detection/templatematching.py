import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


def annotationAdjustment(rect, ref_img_name, target_img_name):

    x = int(round(rect[0]))
    y = int(round(rect[1]))
    delta_y = int(round(rect[2]))
    delta_x = int(round(rect[3]))

    # how much the original rectangle in enlarged for defininf the search space
    step_x = 250
    step_y = 150

    DIR = os.path.dirname(os.path.abspath(__file__))

    ref_img = cv2.imread(DIR + ref_img_name, 0)
    w_ref_img, h_ref_img = ref_img.shape[::-1]
    target_img = cv2.imread(DIR + target_img_name, 0)
    print DIR + ref_img_name , '\n', DIR + target_img_name
    template = ref_img.copy()
    template = template[y:y+delta_y, x:x+delta_x]

    y1 = max(0,y - step_y)
    y2 = min(y+delta_y+step_y, h_ref_img)
    x1 = max(0,x - step_x)
    x2 = min(x+delta_x+step_x, w_ref_img)

    augmented = target_img.copy()
    augmented = augmented[y1:y2, x1:x2]
    w_target_img, h_target_img = delta_x, delta_y #template.shape[::-1]

    method = eval('cv2.TM_CCOEFF')

    # Apply template Matching
    res = cv2.matchTemplate(augmented, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    peak_loc = np.where(res==max_val)
    peak_loc = (peak_loc[0][0] + y1, peak_loc[1][0] + x1)
    print peak_loc

    top_left = max_loc
    tl0 = top_left[0] + x1
    tl1 = top_left[1] + y1
    top_left = (tl0, tl1)
    bottom_right = (top_left[0] + w_target_img, top_left[1] + h_target_img)

    print 'Max loc: ', max_loc, 'X: ', (x1,y1), 'Top left: ', top_left, '\nBottom right: ', bottom_right
    cv2.rectangle(target_img, top_left, bottom_right, 255, 2)
    cv2.circle(target_img, peak_loc, 50, [255,255,255], -10)
    plt.imshow(target_img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()

    return top_left


if __name__ == '__main__':

    rect = [367, 124, 1002, 2223]
    ref_img_name = '/img/001.jpg'
    target_img_name = '/img/002.jpg'

    annotationAdjustment(rect, ref_img_name, target_img_name)










