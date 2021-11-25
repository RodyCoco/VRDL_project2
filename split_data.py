import shutil
import mat73
from data_gen import DigitDataset, get_all_image_size
import os
num = 33402

# for i in range(1,num+1):
#     shutil.copyfile(f"train/train/{i}.png", f"../Street-View-House-Numbers-Detection/data/svhn/train/{i}.png")

# shutil.copytree("../my_dataset", "../yolov5/my_dataset", symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

shutil.copytree("../VRDL_project2", "../VRDL_project2_ver2", symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

# image_size_list = get_all_image_size("train/train",33402)
# digit_data_answer_dict = mat73.loadmat('./train/train/digitStruct.mat',use_attrdict=True)

# for j in range(1,num+1):
#     des = "../Street-View-House-Numbers-Detection/data/svhn/train/"
#     file=open(des+f"{j}.txt","w")
#     data = digit_data_answer_dict["digitStruct"]["bbox"][j-1]
#     w, h = image_size_list[j-1]
#     L =len(data["height"]) if type(data["height"]) == list else 1
#     if L >1 :
#         for i in range(L):
#             if data['label'][i] == 10:
#                 label = 0
#             else:
#                 label = int(data['label'][i])
#             height, left, top, width = data['height'][i], data['left'][i], data['top'][i], data['width'][i]
#             center_x, center_y, box_w, box_h = (left+width/2)/w, (top+height/2)/h, width/w, height/h
#             s = "{} {} {} {} {}\n".format(label, center_x, center_y, box_w, box_h)
#             file.write(s)
#     else:
#         if data['label']== 10:
#             label = 0
#         else:
#             label = int(data['label'])
#         height, left, top, width = data['height'], data['left'], data['top'], data['width']
#         s = "{} {} {} {} {}\n".format(label, center_x, center_y, box_w, box_h)
#         file.write(s)
#     file.close()
