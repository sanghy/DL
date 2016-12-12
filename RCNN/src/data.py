#coding:utf-8
"""
Author:wepon
Source:https://github.com/wepe
file:data.py
"""

import os
from PIL import Image
import numpy as np
import sys
import vocabulary

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
    data = np.empty((100,1,50,200),dtype="float32")
    label = [] #np.empty((100,),dtype=np.str_)
    testfolder="/home/sanghy/Data/DL/train-tow"
    imgs = os.listdir(testfolder)
    num = len(imgs)
    for i in range(num):
        if (i >= 100):
            break
        rgbImage=Image.open(testfolder+"/"+imgs[i])
        img = rgbImage.convert("L")
        arr = np.asarray(img,dtype="float32")
        data[i,:,:,:] = arr
        label_str=str(imgs[i].split('_')[1].split('.')[0]).decode('utf-8')
        ids=np.empty(len(label_str),np.int32)
        for j,char in enumerate(label_str):
            CHAR_VOCABULARY, CHARS = vocabulary.GetCharacterVocabulary()
            ids[j]=np.int32(CHAR_VOCABULARY[char])
        # print(ids)
        label.append(ids)
    label=np.array(label)
    # print(label)
    return data,label

def load_datateststr():
    data = np.empty((100,1,50,200),dtype="float32")
    label = []
    testfolder="/home/sanghy/Data/DL/train-tow"
    imgs = os.listdir(testfolder)
    num = len(imgs)
    for i in range(num):
        if (i >= 100):
            break
        rgbImage=Image.open(testfolder+"/"+imgs[i])
        img = rgbImage.convert("L")
        arr = np.asarray(img,dtype="float32")
        data[i,:,:,:] = arr
        label_str=str(imgs[i].split('_')[1].split('.')[0]).decode('utf-8')
        ids=np.empty(len(label_str),np.str_)
        for j,char in enumerate(label_str):
            CHAR_VOCABULARY, CHARS = vocabulary.GetCharacterVocabulary()
            ids[j]=np.int32(CHAR_VOCABULARY[char])
        label.append(ids)
    #label=np.array(label)
    print(label)
    return data,label

load_datateststr()