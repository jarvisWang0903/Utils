import random
import os
img_file_path = r'C:\Users\ycwang\Desktop\idd_val.txt'
lbl_file_path = r'C:\Users\ycwang\Desktop\idd_val_label.txt'
image_path = r'C:\迅雷下载\idd-segmentation\IDD_Segmentation\leftImg8bit\val'


if __name__ == '__main__':
    image_list = []
    for root, dirs, files in os.walk(top=image_path):
        for dir in dirs:
            path = os.path.join(image_path, dir)
            for root, dirs, files in os.walk(top=path):
                for name in files:
                    image_list.append('leftImg8bit/val/'+ dir + '/' + name)
    img_fin = open(img_file_path, 'w')
    lbl_fin = open(lbl_file_path, 'w')
    for idx, name in enumerate(image_list):
        #'leftImg8bit/train/0/005506_leftImg8bit.png'
        #'gtFine/train/0/005506_gtFine_labelcsTrainIds.png'
        img_fin.write(name + '\n')
        lbl_name = name.split('/',1)[1].split('_')[0]
        lbl_name = str('gtFine/' + lbl_name + '_gtFine_labelcsTrainIds.png')
        lbl_fin.write(lbl_name + '\n')

    img_fin.close()
    lbl_fin.close()
    print(len(image_list))