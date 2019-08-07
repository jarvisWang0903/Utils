import pickle
import numpy as np
root = r'C:\Users\ycwang\Desktop\all_res.pkl'

with open(root, 'rb') as f:
    all_res = pickle.load(f)
    max = 0
    max_key = ''
    for key in all_res.keys():
        mIoUs = all_res[key]
        mIoU = round(np.mean(mIoUs[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15,16, 17, 18]]) * 100, 2)
        if mIoU > max:
            max = mIoU
            max_key = key
    print(max)
    print(max_key)

