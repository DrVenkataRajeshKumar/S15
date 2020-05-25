# S15

## A Large Custom DataSet is created:
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

## Changing the code into Modilar ["code"](https://github.com/DrVenkataRajeshKumar/S15/blob/master/modularcode.ipynb)

## implementing the code onto entire 400k Dataset ["code"](https://github.com/DrVenkataRajeshKumar/S15/blob/master/S15Final.ipynb)


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






## A Large Custom DataSet is created using few images with fallowing steps
* Cars were chosed as Foreground(fg) images and
* Streets & Roads were chosed a Backgroung(bg) images.

## Data set of 100 Backgroung images of streets & roads   
### [link to bg images](https://drive.google.com/open?id=1nc1Yi_p7G7qDY8Gsl42keVgg6t-AQyGh)    
* Background images were downloaded and resized to 224* 224 uing GIMP
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/9.png)


## Data set of 100 Foreground images of cars   
### [link to fg images](https://drive.google.com/open?id=1WFGmx-W2OBwhcEuqEANuUtc5JnRvtKA9)   
* car images were downloaded, backgrounds were deleted uing 3Dpaint and car images with tranparent background were created.
 *Regreted this step in later stages of creating depth images- as it created blur margins
 
 ![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/97.png)




## Data set of 100 Masks of Foreground images 
* Masks are the images with the object in white colour and remaining part in dark black colour.
* Tried using 3Dpaint and GIMP for creating masks of foreground images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/masks.png)





## Data set of 400k overlay images of Foreground on Background  
### ["link to Overlay images"](https://drive.google.com/open?id=1c8tO4rYzJtpDFUu5bJ0XBE9uvtl6ZWzH)  
Tried different approaches for overlay of foreground on background images.  
* Tried GIMP- water mark tool. managed to create 1000 images at a time.  
* In search of better approach used Photoshop. Recorded actions and implemented in scripts for automation for working on multiple sets of images. Managed to create 10000 images at a time i.e. placing one foreground image at 10 different places on all background images. Problem with this approach was it took almot 1hour for creating implementations and scripts and generating 10000 images. And more frustrating part is, have to creat scripts for new foreground each and every time. That means have to work 100 hour to implement with 100 foreground images.  
* Finally understood the value of coding and loop implementation. 

* Started coding in colab. 
* Next problem encountered was to handle large number of images generated in colab.
Used zip folder, to flush, generated images into zipfile.
Finally after several attempts able to generate 400k fgbg and fgbg_mask images in jest 1 hour 30 minutes and able to store them in zip file with-out colapsing the drive. [code](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/trail15a.ipynb)
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/overlay.png)

## 400k Masks of overlayed images
### [link to Masks of overlay images](https://drive.google.com/open?id=1og3tDEszR1N6lqEZsc6DE3s-9EG3cfzp)
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/overlay%20mask.png)


## Depth estimation of 400k overlay images   
### [link to Depth images](https://drive.google.com/open?id=1JUupNIBdN-oZdGwyctPhyzOPpKqO3_86)   
* Tried the Depth model reference given [DenseDepth nyu-h5](https://github.com/ialhashim/DenseDepth/blob/master/DenseDepth.ipynb) and with few modifications able to implement nyu-h5 on the overlay bg-fg images.    
Depth predictions were not prominent. 
 
* Tried [KITTI ICCV](https://github.com/nianticlabs/monodepth2) and foundout better depth predictions than nyu-h5. My intusion for poor depth prediction of few fg images is (*As menctioned erlier) becaue of poor selection of foregroung images i.e with blur margins
* [Code for Depth images](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/depth.ipynb)   
* KITTI is used for outdore images, and nyu-h5 is mostly used for indore images.
* KITTI predicts nearer objects with lighter colour, Where as nyu-h5 predicts farther objects with lighter colour

![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/depth.png)


## Custom DataSet
* Overlay images [link](https://drive.google.com/open?id=1c8tO4rYzJtpDFUu5bJ0XBE9uvtl6ZWzH)
* Masks of Overlay images [link](https://drive.google.com/open?id=1og3tDEszR1N6lqEZsc6DE3s-9EG3cfzp)
* Lables of images [link](https://drive.google.com/open?id=1Qcd7u3Qy-Pm7XCW4TKQX5A62jjAFnQrL)
* Depth images [link](https://drive.google.com/open?id=1JUupNIBdN-oZdGwyctPhyzOPpKqO3_86)
