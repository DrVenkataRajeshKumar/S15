# S15

## A Large Custom DataSet is created(S15-A):
### [link to Discription of DataSet creation](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/README.md)
400000 images were created using only 100 foreground images and 100 background images
* Background images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/9.png)
* Foreground images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/97.png)
* Overlay images of Foreground on Background
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/overlay.png)
* Masks of Overlay images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/overlay%20mask.png)
* Depth images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/depth.png)


## Problem Statement:
"Have to generate Overlay masks and Depth images by DNN training of FgBg images and Bg images, without using opensource"


### Basic architecture with small Data ["code"](https://github.com/DrVenkataRajeshKumar/S15/blob/master/15_trail.ipynb)
Initially set of 7800 images were taken as a group to tryout the basic architecture of code.  
100 Bg images, 7800 FgBg images and corresponding 7800 mask images of FgBg, 7800 Depth images were taken as Dataset.  
only Bg images and FgBg images were used in training.  
FgBg masks and Depth images were used to compare prediction and calculating loss'


* Tried transforms resize to small size to handle burden on the GPU.  
* Tried gray scale transform because of 2 reasons.  
**  1. as our predictions i.e mask images and depth images are in gray scale    
**  2. to reduce the burden on GPU by reducing the weights, channels 
Ploted the images after transforms.


* 1st issue encountered was to train 2 sets of images simultaniouly.  
DNNcode was modified so that it trains both set of images(bg and fgbg images) simultaniouly.

* 2 DNNs were used in this process.
One is to calculate loss, and another one is to implement loss and predict Mask images and Depth images.
While coding DNN, one has to choose between wider network or deep network.
Wider networks can be used when number of classes to be predicted are more.
Where as deeper networks will be advantgeous when multiple varients are present in given classes. 

* Tried serching documentations for different loss functions and their implimentations.
Tried different loss functons and endedup with using "BCEWithLogitsLoss"


* Then the next issue to be addressed is ploting the loss and predictions..
Tried implementing tensorboard, but couldnt figureout cirtain issues.
Endedup by ploting the image per each epoch i.e loss for mask images, loss for depth images, then mask prediction and deph prediction anf original fgbg image.

* Trained for 2 epochs

* Trained for 5 epochs and oberved the variations in predictions [code](https://github.com/DrVenkataRajeshKumar/S15/blob/master/15_trail_on_21_may.ipynb)

* Trained for 20 epochs and oberved the variations in predictions [code](https://github.com/DrVenkataRajeshKumar/S15/blob/master/20epochs.ipynb)


## Changes in loss function ["code"](https://github.com/DrVenkataRajeshKumar/S15/blob/master/22may.ipynb)
* Till now only BCEWithLogitsLoss was used for both Mask image loss calculation and Depth image loss calculation.
* SSIM is used for Depth images and BCEWithLogitsLoss is contined for mask images.

## Changing the code into Modular ["code"](https://github.com/DrVenkataRajeshKumar/S15/blob/master/modularcode.ipynb)  
Converted code into modular code.  
### [Library link](https://github.com/DrVenkataRajeshKumar/S15/tree/master/Library)


## Implementing the code onto entire 400k Dataset ["code"](https://github.com/DrVenkataRajeshKumar/S15/blob/master/S15Final.ipynb)


* ploted images of Mask prediction loss  
![Image](https://github.com/DrVenkataRajeshKumar/S15/blob/master/l%20m1.png)
* ploted images of Depth prediction loss  
![Image](https://github.com/DrVenkataRajeshKumar/S15/blob/master/l%20d%201.png)
* ploted images of mask predictions  
![Image](https://github.com/DrVenkataRajeshKumar/S15/blob/master/m1.png)
* ploted images of Depth predictions  
![Image](https://github.com/DrVenkataRajeshKumar/S15/blob/master/d1.png)
* FgBg images  
![Image](https://github.com/DrVenkataRajeshKumar/S15/blob/master/fgbg1.png)





