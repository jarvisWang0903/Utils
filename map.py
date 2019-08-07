import numpy as np
from PIL import Image
import os
import tqdm
root_path = r'C:\data\gta5\labels'
save_path = r'C:\data\gta5\map_labels'
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

def SegColor2Label(img, mapMatrix):
    """
    img: Shape [h, w, 3]
    mapMatrix: color-> label mapping matrix,
               覆盖了Uint8 RGB空间所有256x256x256种颜色对应的label

    return: labelMatrix: Shape [h, w], 像素值即类别标签
    """
    data = img.astype('int32')
    indices = data[:, :, 0] * 65536 + data[:, :, 1] * 256 + data[:, :, 2]
    return mapMatrix[indices]

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
    mapMatrix = 255 * np.ones(256 * 256 * 256, dtype=np.int32)
    for i, cm in enumerate(common_valid_colors):
        mapMatrix[cm[0] * 65536 + cm[1] * 256 + cm[2]] = i

    for root, dirs, files in os.walk(top=root_path):
        tbar = tqdm.tqdm(files)
        for img in tbar:
            path = os.path.join(root_path, img)
            saved_path = os.path.join(save_path, img)
            color_img = Image.open(path).convert('RGB')
            image = np.asarray(color_img)
            mask = SegColor2Label(image, mapMatrix)
            img_ = Image.fromarray(mask, mode='I')
            img_.save(saved_path)
