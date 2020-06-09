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
The usage of the following python files is given as follows:
* **preprocess_human36.py** contains all functions for preprocessing the Human 3.6M dataset. 
* **preprocess_ntu.py** contains all functions for preprocessing the NTURGB-D dataset. 
* **train.py** is used for training the model. Here, the bidirectional GAN has been used with the frame-wise geodesic loss along with recursive  prediction strategy to avoid mode-collapse and to further regularize the training.
* The **bodyjoints_to_array.py** file uses the SequenceBodyReader class which prepares a batch of sequence of bodies for each clip and other functions such as next_minibatch() to give a mini batch of sequences and their ground truth, select_frames() to fixed sequence length from the provided clip, and from_body_to_feature() to converty body joints to a numpy array and apply the needed normalization.
* The **gan_neural_network.py** file contains the main neural network whereas the files **human36_poses.py** and **ntu_poses.py** have functions which are used to read and parse the Human3.6M and NTURGB-D skeleton files. 


## Dataset
I have used the 3D skeleton data from NTU-RGBD and Human 3.6m dataset to train HP-GAN:

NTU-RGBD: http://rose1.ntu.edu.sg/datasets/actionrecognition.asp <br>
Human 3.6m: http://vision.imar.ro/human3.6m/description.php <br>
For Human 3.6m, the h5 format and parsing code is obtained from https://github.com/una-dinosauria/3d-pose-baseline

## Results
Sample output for the eating pose <br>
<img src= "https://github.com/abhishek-924/GAN-Poser/blob/master/img/eating.png" width="20%" height= "20%">
<br><br>
Sample output for the walking pose <br>
<img src= "https://github.com/abhishek-924/GAN-Poser/blob/master/img/walking.png" width="20%" height= "20%">
 
## Citation
If you're using this repository or my publication for your research, kindly cite the following:

```
@article{jain2020gan,
  title={GAN-Poser: an improvised bidirectional GAN model for human motion prediction},
  author={Jain, Deepak Kumar and Zareapoor, Masoumeh and Jain, Rachna and Kathuria, Abhishek and Bachhety, Shivam},
  journal={Neural Computing and Applications},
  pages={1--13},
  year={2020},
  publisher={Springer},
}
```

