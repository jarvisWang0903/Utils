from PIL import Image
import numpy as np

if __name__ == '__main__':
    image = Image.open(r'C:\Users\ycwang\Desktop\lindau_000044_000019_gtFine_labelIds.png')
    image = np.array(image)
    print(np.unique(image))