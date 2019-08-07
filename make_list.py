import random
import os
#img_file_path = r'C:\Users\ycwang\Desktop\image_list\bdd100k_train.txt'
file_path = r'C:\Users\ycwang\Desktop\data_list\city_sybthia_idd_list\city_bdd_idd_val_old.txt'
lbl_path = r'C:\Users\ycwang\Desktop\data_list\city_sybthia_idd_list\city_bdd_idd_val_label_old.txt'
sample = r'C:\Users\ycwang\Desktop\data_list\city_sybthia_idd_list\city_bdd_idd_val.txt'
sample_label = r'C:\Users\ycwang\Desktop\data_list\city_sybthia_idd_list\city_bdd_idd_val_label_sample.txt'
import numpy as np

if __name__ == '__main__':
    image_list = []
    lbl_list = []
    img_fin = open(file_path, 'r')
    lbl_fin = open(lbl_path, 'r')
    sample_fin = open(sample, 'w')
    sample_label_fin = open(sample_label, 'w')

    for name in img_fin:
        image_list.append(name)
    for name in lbl_fin:
        lbl_list.append(name)
    np.random.seed(1)
    np.random.shuffle(image_list)
    np.random.seed(1)
    np.random.shuffle(lbl_list)
    for i in range(len(image_list)):
        img_name = image_list[i]
        lbl_name = lbl_list[i]
        sample_fin.write(img_name)
        sample_label_fin.write(lbl_name)

    print(len(image_list))

