from PIL import Image
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

def decode_segmap(img, dataset, nun_class=19):
    '''
    decoder img to RGB img
    :param img: shape[h, w]
    :param dataset: cityscapes or bdd100k
    :return: map [n, h, w, c]
    '''
    if dataset.lower() in ['cityscapes', 'gta5', 'sythia','bdd100k']:
        label_colours = common_label_colours
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
    from shutil import copyfile
    import os
    import os.path as osp
    from tqdm import tqdm
    root = r'C:\Users\ycwang\Desktop\222.png'
    # target_path = osp.join(r'C:\XLdownload','appolo_color_label_train')
    # if not osp.exists(target_path):
    #     os.makedirs(target_path)
    # img_list = open(r"C:\Users\ycwang\Desktop\data_list\apollo_list\train_label_sample.txt")
    # id_to_trainid = {49: 0, 50: 1, 97: 2, 84: 3, 67: 4, 82: 5, 81: 6, 83: 7, 113: 8,
    #                  36: 11, 164: 11, 33: 13, 161: 13, 17: 10,
    #                  38: 14, 166: 14, 39: 15, 167: 15, 34: 17, 162: 17, 35: 18, 163: 18}
    # for name in tqdm(img_list):
    #     splits = name.split('/')
    #     new_name = ''
    #     for split in splits:
    #         new_name += split + '\\'
    #     img_path = osp.join(root,new_name.rstrip('\\').rstrip())
    #     img = Image.open(img_path)
    #     image = np.asarray(img)
    #     label_copy = 255 * np.ones(image.shape, dtype=np.long)
    #     for k, v in id_to_trainid.items():
    #         label_copy[image == k] = v
    #     map = decode_segmap(label_copy, 'sythia', 19)
    #     imgs_s = np.clip(map * 255, 0, 255).astype(np.uint8)
    #     imgs_s = Image.fromarray(imgs_s)
    #     save_path = osp.join(target_path,new_name.rstrip('\\').rstrip().rsplit('\\', 1)[-1])
    #     imgs_s.save(save_path)
    img = Image.open(root)
    image = np.asarray(img)
    #map = decode_segmap(image, 'bdd100k', 19)
    #imgs_s = np.clip(map * 255, 0, 255).astype(np.uint8)
    #imgs_s = Image.fromarray(imgs_s)
    #imgs_s.save(r'C:\Users\ycwang\Desktop\color_img_111.png')
    print(np.unique(img))
    #[  0   1   2   5   7   8   9  10  11  12  13  14  17 255]
