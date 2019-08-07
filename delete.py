import os
import numpy as np
import torch.nn as nn
import torch
from deeplab import Res_Deeplab


if __name__ == '__main__':
    restore_from=r"/home/groupprofzli/data1/ycwang/model/res101_gta_no_adapt.pth"

    state_dict = torch.load(restore_from, map_location=lambda storage, loc: storage)
    model = Res_Deeplab(19)
    new_params = model.state_dict().copy()
    encoder = state_dict['encoder']
    decoder = state_dict['decoder']

    #print(decoder.keys())
    #print(new_params.keys())
    for i in encoder:
        i_parts = i.split('.',1)[-1].split('.')
        if i.split('.',1)[-1] in new_params.keys():
            new_params[i.split('.',1)[-1]] = encoder[i]
        else:
            tmp = i.split('.',1)[-1].split('.',1)[-1]
            if tmp in decoder.keys():
                new_params[] = decoder[tmp]

            #new_params['layer5.conv2d_list.2.weight'] = encoder[i]
    #model.load_state_dict(new_params)
