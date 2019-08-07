from shutil import copyfile
import os
import os.path as osp
import numpy as np
common_valid_colors = [[128, 64, 128],  # Road, 0
                      [244, 35, 232],  # Sidewalk, 1
                      [70, 70, 70],  # Building, 2
                      [102, 102, 156],  # Wall, 3
                      [190, 153, 153],  # Fence, 4
                      [153, 153, 153],  # pole, 5
                      [250, 170, 30],  # traffic light, 6
                      [220, 220, 0],  # traffic sign, 7
                      [107, 142, 35],  # vegetation, 8
                      [152, 251, 152],  # terrain, 9
                      [70, 130, 180],  # sky, 10
                      [220, 20, 60],  # person, 11
                      [255, 0, 0],  # rider, 12
                      [0, 0, 142],  # car, 13
                      [0, 0, 70],  # truck, 14
                      [0, 60, 100],  # bus, 15
                      [0, 80, 100],  # train, 16
                      [0, 0, 230],  # motor-bike, 17
                      [119, 11, 32]]  # bike, 18
# in the 16-class setting: removing index 9, 14, 16

common_label_colours = dict(zip(range(19), common_valid_colors))

apollo_valid_colors = [[128, 64, 128],  # Road, 0
                       [244, 35, 232],  # Sidewalk, 1
                       [70, 70, 70],  # Building, 2
                       [102, 102, 156],  # Wall, 3
                       [190, 153, 153],  # Fence, 4
                       [153, 153, 153],  # pole, 5
                       [250, 170, 30],  # traffic light, 6
                       [220, 220, 0],  # traffic sign, 7
                       [107, 142, 35],  # vegetation, 8
                       [255, 255, 255], #terrain, 9
                       [255, 255, 255],  # sky, 10
                       [220, 20, 60],  # person, 11
                       [255, 255, 255],  # rider, 12
                       [0, 0, 142],  # car, 13
                       [0, 0, 70],  # truck, 14
                       [0, 60, 100],  # bus, 15
                       [255, 255, 255],  # train, 16
                       [0, 0, 230],  # motor-bike, 17
                       [119, 11, 32]]  # bike, 18
apollo_label_colours = dict(zip(range(19), apollo_valid_colors))

def decode_segmap(img, dataset, nun_class=19):
    '''
    decoder img to RGB img
    :param img: shape[h, w]
    :param dataset: cityscapes or bdd100k
    :return: map [n, h, w, c]
    '''
    if dataset.lower() in ['cityscapes', 'gta5', 'sythia','bdd100k']:
        label_colours = common_label_colours
    elif dataset.lower() in ['apollo']:
        label_colours = apollo_label_colours
    else:
        raise NotImplementedError
    map = np.zeros((img.shape[0], img.shape[1], 3))
    r = img.copy()
    g = img.copy()
    b = img.copy()
    for l in range(0, nun_class):
        r[img == l] = label_colours[l][0]
        g[img == l] = label_colours[l][1]
        b[img == l] = label_colours[l][2]

    rgb = np.zeros((img.shape[0], img.shape[1], 3))
    rgb[:, :, 0] = r / 255.0
    rgb[:, :, 1] = g / 255.0
    rgb[:, :, 2] = b / 255.0
    map[ :, :, :] = rgb
    return map


if __name__ == '__main__':

    root = r'C:\XLdownload\road02_seg'
    target_path = osp.join(r'C:\XLdownload','appolo_train')
    if not osp.exists(target_path):
        os.makedirs(target_path)
    img_list = open(r"C:\Users\ycwang\Desktop\data_list\apollo_list\train_sample.txt")
    for name in img_list:
        splits = name.split('/')
        new_name = ''
        for split in splits:
            new_name += split + '\\'
        img_path = osp.join(root,new_name.rstrip('\\').rstrip())
        save_path = osp.join(target_path,new_name.rstrip('\\').rstrip().rsplit('\\', 1)[-1])
        copyfile(img_path, save_path)
    # img = Image.open(r'C:\Users\ycwang\Desktop\mode.png')
    # img = Image.open(r'C:\Users\ycwang\Desktop\11.png')
    # image = np.asarray(img)
    # encode = encoder(image, common_label_colours)
    # print(np.unique(encode))
    # print(encode.shape)
    # encode_img = Image.fromarray(encode, mode='I')
    # encode_img.save(r'C:\Users\ycwang\Desktop\encode_img.png')
    # img = np.array(Image.open(r'C:\Users\ycwang\Desktop\encode_img.png'))
    # print(np.unique(img))

    # map = decode_segmap(img, 'bdd100k', 19)
    # imgs_s = np.clip(map * 255, 0, 255).astype(np.uint8)
    # # imgs_s = imgs_s[0].transpose(1, 2, 0)
    # imgs_s = Image.fromarray(imgs_s)
    # imgs_s.save(r'C:\Users\ycwang\Desktop\color_img.png')