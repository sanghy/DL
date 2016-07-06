#coding:utf-8
"""
Author:wepon
Source:https://github.com/wepe
file:data.py
"""

import os
from PIL import Image
import numpy as np

def load_data():
    data = np.empty((200000,3,200,50),dtype="float32")
    label = np.empty((200000,),dtype="uint8")
    trainfolder="/home/sanghy/Data/DL/train-one"
    imgs = os.listdir(trainfolder)
    num = len(imgs)
    for i in range(num):
        if (i >= 200000):
            break
        try:
            img = Image.open(trainfolder + "/" + imgs[i])
            arr = np.asarray(img, dtype="float32")
            data[i, :, :, :] = arr
            label[i] = str(imgs[i].split('.')[0].split('_')[2])
        except Exception,e:
            print(img)
            print e

    return data,label


def load_datatest():
    data = np.empty((100,50,200,3),dtype="float32")
    label = np.empty((100,),np.str_)
    testfolder="/home/sanghy/Data/DL/train-tow"
    imgs = os.listdir(testfolder)
    num = len(imgs)
    for i in range(num):
        if (i >= 100):
            break
        img = Image.open(testfolder+"/"+imgs[i])
        arr = np.asarray(img,dtype="float32")
        data[i,:,:,:] = arr
        label[i] = str(imgs[i].split('.')[0].split('_')[0])
        # print(str(imgs[i].split('.')[0].split('_')[0]))
    return data,label