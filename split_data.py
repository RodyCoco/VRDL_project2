import shutil
import mat73
from data_gen import DigitDataset, get_all_image_size
import os
num = 33402

for j in range(1, num+1):
    if j % 10 <= 7:
        des = "my_dataset/images/train/"
    else:
        des = "my_dataset/images/valid/"
    shutil.copyfile(
        "my_dataset/images/proprecess_train/{j}.png", des+"{j}.png")

image_size_list = \
    get_all_image_size("my_dataset/images/preprocess_train", 33402)
digit_data_answer_dict = \
    mat73.loadmat(
        'my_dataset/images/preprocess_train/digitStruct.mat',
        use_attrdict=True)

for j in range(1, num+1):
    if j % 10 <= 7:
        des = "my_dataset/labels/train/"
    else:
        des = "my_dataset/labels/valid/"
    file = open(des+f"{j}.txt", "w")
    data = digit_data_answer_dict["digitStruct"]["bbox"][j-1]
    w, h = image_size_list[j-1]
    L = len(data["height"]) if type(data["height"]) == list else 1
    if L > 1:
        for i in range(L):
            if data['label'][i] == 10:
                label = 0
            else:
                label = int(data['label'][i])
            height, left, top, width =\
                data['height'][i], data['left'][i],\
                data['top'][i], data['width'][i]
            center_x, center_y, box_w, box_h = \
                (left+width/2)/w, (top+height/2)/h, width/w, height/h
            s = "{} {} {} {} {}\n" \
                .format(label, center_x, center_y, box_w, box_h)
            file.write(s)
    else:
        if data['label'] == 10:
            label = 0
        else:
            label = int(data['label'])
        height, left, top, width = \
            data['height'], data['left'], data['top'], data['width']
        s = "{} {} {} {} {}\n".format(label, center_x, center_y, box_w, box_h)
        file.write(s)
    file.close()
