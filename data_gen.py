import os
from PIL import Image
import torch.utils.data as data
import natsort
import torchvision.transforms as tfs

GPU_NUMBER = 0

class DigitDataset(data.Dataset):
    def __init__(self, data, main_dir, transform):
        super(DigitDataset, self).__init__()
        self.main_dir = main_dir
        self.transform = transform
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_loc = os.path.join(self.main_dir, f"{self.data[idx]}.png")
        image = Image.open(img_loc).convert("RGB")
        image = self.transform(image)
        return image, self.data[idx]-1
    
def get_all_image_size(main_dir, num):
    image_size_list = []
    for i in range(1,num+1):
        img_loc = os.path.join(main_dir, f"{i}.png")
        image = Image.open(img_loc).convert("RGB")
        # image = image.crop((77, 29, 77+23, 29+32))  # (left, upper, right, lower)
        image_size_list.append(image.size)
    return image_size_list

