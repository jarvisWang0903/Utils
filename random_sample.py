import numpy as np
import random
list_path = r'C:\Users\ycwang\Desktop\train.txt'
train_list_path = r'C:\Users\ycwang\Desktop\train_sample.txt'
#train_label_list_path = r'C:\Users\ycwang\Desktop\train_label_sample.txt'

#val_path = r'C:\Users\ycwang\Desktop\val.txt'
val_list_path = r'C:\Users\ycwang\Desktop\val_sample.txt'
#val_label_list_path = r'C:\Users\ycwang\Desktop\val_label_sample.txt'
if __name__ == '__main__':
    train_image_list = []
    #val_image_list = []
    #fin_val = open(val_path, 'r')
    fin_train = open(list_path, 'r')
    for name in fin_train:
        train_image_list.append(name)
    # for name in fin_val:
    #     val_image_list.append(name)
    random.shuffle(train_image_list)
    #random.shuffle(val_image_list)

    # train sample
    train_fin_sample = open(train_list_path, 'w')
    #train_label_fin_sample = open(train_label_list_path, 'w')
    for i in range(10000):
        name = train_image_list[i]
        label_name = str(name)
        train_fin_sample.write(name)
        #train_label_fin_sample.write(label_name + '\n')
    # val sample
    val_fin_sample = open(val_list_path, 'w')
    #val_label_fin_sample = open(val_label_list_path, 'w')
    for i in range(10000, 11000):
        name = train_image_list[i]
        #label_name = str(name)
        val_fin_sample.write(name)
        #val_label_fin_sample.write(label_name + '\n')

    #fin_val.close()
    fin_train.close()
    #train_label_fin_sample.close()
    train_fin_sample.close()
    #val_label_fin_sample.close()
    val_fin_sample.close()
    print(len(train_image_list))
    # random.shuffle(list1)