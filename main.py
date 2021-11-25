import mat73
import torch
import torch.hub
import numpy as np
import skimage.io
import matplotlib.pyplot as plt
import torchvision.transforms as tfs

from torch.utils.data import DataLoader
from PIL import Image
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from data_gen import DigitDataset, get_all_image_size

lr = 5e-6
epochs = 200
batch_size = 32
number_of_data = 33402

train_trans = tfs.Compose([
    tfs.Resize((56, 56), Image.BILINEAR),
    tfs.RandomHorizontalFlip(),
    tfs.RandomRotation(degrees=45),
    tfs.ToTensor(),
    # tfs.Normalize(mean=[0.5, 0.5, 0.5], std=[0.2, 0.2, 0.2])
])

valid_trans = tfs.Compose([
    # tfs.Resize((56, 56), Image.BILINEAR),
    tfs.ToTensor(),
    # tfs.Normalize(mean=[0.5, 0.5, 0.5], std=[0.2, 0.2, 0.2])
])


def procedure():
    
    torch.manual_seed(0)
    torch.cuda.manual_seed(0)
    torch.cuda.manual_seed_all(0)
    np.random.seed(0)
    
    model = torch.hub.load("VCasecnikovs/Yet-Another-YOLOv4-Pytorch", "yolov4", pretrained=True)
    # digit_data_answer_dict = mat73.loadmat('./train/train/digitStruct.mat',use_attrdict=True)
    # digit_data_answer_dict["digitStruct"]["bbox"][0] 
    # digit_data_answer_dict["digitStruct"]["name"][0]
    
    train_data = []
    valid_data = []
    image_size_list = get_all_image_size("train/train",33402)
    
    for i in range(1, number_of_data+1):
        if i%10<=7 :
            train_data.append(i)
        else:
            valid_data.append(i)
            
    train_data = DigitDataset(
        main_dir="train/train",
        data = train_data,
        transform=valid_trans)
    train_loader = DataLoader(
        dataset=train_data, batch_size=batch_size, shuffle=True)
    
    valid_data = DigitDataset(
        main_dir="train/train",
        data = valid_data,
        transform=valid_trans)
    valid_loader = DataLoader(
        dataset=valid_data, batch_size=batch_size, shuffle=True)
    
    # for index, (x, y) in enumerate(train_loader):
    #     # print(digit_data_answer_dict["digitStruct"]["name"][int(y[0])])
    #     print(y[0])
    #     plt.imshow(x[0].permute(1, 2, 0))
    #     plt.savefig("123.png")
    #     input()

    

if __name__ == '__main__':
    procedure()