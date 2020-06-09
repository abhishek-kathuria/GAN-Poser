# GAN-Poser: An Improvised Bidirectional GAN Model for Human Motion Prediction <br>
This repository implements the code behind GAN-Poser publication (https://link.springer.com/article/10.1007/s00521-020-04941-4).

## Introduction
This project is a part of my final project of undergraduation and it uses a novel method called GAN-Poser to predict human motion in less time; given an input 3D human skeleton sequence based on a generator discriminator framework. It uses the Bidirectional GAN framework along with a recursive prediction strategy to avoid mode-collapse and to further regularize the training. The model takes as input a 3D sequence of previous poses and a random vector z from the reduced sequence area that samples attainable future poses. For every such z value, the model generates a special output sequence of attainable future poses
The dataset used is the standard **NTU-RGB-D** and **Human3.6M dataset**. The results obtained helped in the improvement of the predictions of motion sequences from a global outlook.

I have completed this research project under the guidance of [Dr. Deepak Kumar Jain](https://www.linkedin.com/in/deepak-kumar-jain-837b3138/?originalSubdomain=cn). He is an Assistant Professor and Research Scientist at the Chongqing University of Posts and Telecommunications, China. <br><br>
My research paper on titled [**GAN-Poser: An Improvised Bidirectional GAN Model for Human Motion Prediction**](https://link.springer.com/article/10.1007/s00521-020-04941-4) has been published in the **special issue of Deep Learning Approaches for RealTime Image Super Resolution (DLRSR),  Neural Computing and Applications (NCAA)**, which is an SCI-indexed Journal with an impact factor of **4.68**.<br>

## Requirements
* Anaconda
* Tensorflow 1.8 <br>
* h5py
You can either run the code on python 3.6 or on the kaggle kernel GPU.

  
## Usage
Run the files in the following order:
1. **preprocess_human36.py** contains all the libraries to be imported initially. 

## Dataset
I have used the 3D skeleton data from NTU-RGBD and Human 3.6m dataset to train HP-GAN:

NTU-RGBD: http://rose1.ntu.edu.sg/datasets/actionrecognition.asp <br>
Human 3.6m: http://vision.imar.ro/human3.6m/description.php <br>
For Human 3.6m, the h5 format and parsing code is obtained from https://github.com/una-dinosauria/3d-pose-baseline

## Results
![eating](https://github.com/abhishek-924/GAN-Poser/blob/master/img/eating.png)
 
## Citation
If you're using theis repository or the publication for your research, kindly cite the following 

