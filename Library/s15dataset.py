# -*- coding: utf-8 -*-
"""s15dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aAmDlTSAc1ypmMIHgcHpYVlTSFQL3Dbo
"""

from S15 import s15utils
from torchvision import datasets
from torch.utils.data import DataLoader, Dataset , random_split

class MasterDataset(Dataset):
    def __init__(self,  transform= None, bg_files= None, fg_bg_files= None, ms_bg_files= None, dp_files= None):
    
    
        self.bg_files= bg_files
        self.fg_bg_files= fg_bg_files
        self.ms_bg_files= ms_bg_files
        self.dp_files= dp_files

        self.transform = transform

    def __len__(self):
        return len(self.bg_files)

    def __getitem__(self,index):
        bg_image = Image.open(self.bg_files[index])
        fg_bg_image = Image.open(self.fg_bg_files[index])
        ms_bg_image = Image.open(self.ms_bg_files[index])
        dp_image = Image.open(self.dp_files[index])

        if self.transform:
            bg_image = self.transform(bg_image)
            fg_bg_image = self.transform(fg_bg_image)
            ms_bg_image = self.transform(ms_bg_image)
            dp_image = self.transform(dp_image)
        return {'bg_image' : bg_image,'fg_bg_image' : fg_bg_image, 'ms_bg_image' : ms_bg_image, 'dp_image' : dp_image}