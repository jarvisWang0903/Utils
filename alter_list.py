import os.path as osp
from PIL import Image

def alter_list():
    return


if __name__ == '__main__':
    root = r'C:\Users\ycwang\Desktop\data_list\gta5_list\label.txt'

    train_fin = open(path,'r')
    new_train_fin = open(new_path,'w')
    for idx, name in enumerate(train_fin):
        new_name = str('GT/LABELS/' + name.split('/')[-1].strip())
        new_train_fin.write(new_name + '\n')
