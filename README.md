# S15

## A Large Custom DataSet is created
### [link to Diacription of DataSet creatin](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/README.md)
400000 images were created using only 100 foreground images and 100 background images
* Background images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/9.png)
* Foreground images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/97.png)
* Overlay images of Foreground on Background
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/overlay.png)
* Depth images
![Image](https://github.com/DrVenkataRajeshKumar/S15-A/blob/master/depth.png)




set of 7800 images were taken as a group to tryout the initial architecture of code.
100 bg images, 7800 fgbg images and corresponding 7800 mask images of fgbg, 7800 depth images were taken as dataset.


Tried transforms resize to small size to handle burden on the GPU. Tried gray scale transform because of 2 reasons.
1. as our predictions i.e mask images and depth images are in gray scale
2. to reduce the burden on GPU by reducing the weights, channels

only bg image and fgbg images were trained.
1st issue encountered was to train 2 sets of images simultaniouly.
Modified DNNcode so that it trains both set of images(bg and fgbg images) simultaniouly.

to predict mask, Depth images thought of comparing the output layers to the actual masks and depth images and calculate the loss.
this loss will be append to the next batch of images and so on..
Tried serching documentations for different loss functions and their implimentations.
tried different loss functons and endedup with using "BCEWithLogitsLoss"


Then the next issue to be addressed is ploting the loss n predictions..
tried implementing tensorboard, but couldnt figureout cirtain issues.
endedup in just ploting the image per each epoch i.e loss for mask images, loss for depth images, then mask prediction and deph prediction anf original fgbg image.





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
