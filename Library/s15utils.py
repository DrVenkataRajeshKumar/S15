# -*- coding: utf-8 -*-
"""s15utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10sG6SqaODhcNLM8QZF90uCBjlQsbMAvC
"""

# -*- coding: utf-8 -*-
"""s15utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aAmDlTSAc1ypmMIHgcHpYVlTSFQL3Dbo
"""

import torch
import json
import torchvision
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm_notebook, tnrange
import numpy as np
import matplotlib.pyplot as plt
import io
from itertools import groupby
import cv2
from tqdm.auto import tqdm
from pathlib import Path
from time import time
from torchvision import datasets
from torch.utils.data import DataLoader, Dataset , random_split
from PIL import Image
from torchvision.transforms import transforms
import os
from glob import glob
import torch
import torchvision
from torch import nn
#from kornia.losses import SSIM
from torch.optim.lr_scheduler import StepLR