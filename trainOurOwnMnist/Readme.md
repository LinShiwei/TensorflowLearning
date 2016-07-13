# Train mnist using your own images

## Introduction

In [tensorflow.org](http://www.tensorflow.org) there are [MNIST For ML Beginners](https://www.tensorflow.org/versions/r0.9/tutorials/mnist/beginners/index.html) and [Deep MNIST for Experts](https://www.tensorflow.org/versions/r0.9/tutorials/mnist/pros/index.html) for learning. 

In these tutorials, the training source is from [MNIST](http://yann.lecun.com/exdb/mnist/). It is awesome, containing thousands of images.

But there are some situations that we want to use our own images for training. I have searched on the Internet and could hardly find the direct way to convert images into MNIST Database format. So I just do it myself and have found another way to create my data files and train it in the tensorflow.

## Method
###Step One

You should first have some images for training. You can use your own images or use my images for a try. 

The images like the following, should have a black background and a white number.
[image]()

###Step Two

I have writed some Matlab code to convert your images into image data and create label data. These data are in binary format and have '.txt' suffix. Here shows the data format in these data file.

![image](https://raw.githubusercontent.com/LinShiwei/TensorflowLearning/master/trainOurOwnMnist/dataFormat.png)
After generate these four file:
```
trainImage.txt
trainImageLabel.txt
testImage.txt
testImageLabel.txt
```
You should use gzipCreate.py to convert these files into '.gz' file.
```
trainImage.txt.gz
trainImageLabel.txt.gz
testImage.txt.gz
testImageLabel.txt.gz
```
Until now, the training files are ready.(training files can be find in this repository

###Step Three

I have done some changes to tensorflow's mnist example code. You can use lswBeginnerMnist.py for simple mnist training or use lswDeepMnist.py for deep mnist training.

Result of [lswBeginnerMnist.py](https://github.com/LinShiwei/TensorflowLearning/blob/master/trainOurOwnMnist/lswbeginnerMnist.py) training , 29 images.

![image](https://raw.githubusercontent.com/LinShiwei/TensorflowLearning/master/trainOurOwnMnist/beginnerMnistTrainingResult.png)

Result of [lswDeepMnist.py](https://github.com/LinShiwei/TensorflowLearning/blob/master/trainOurOwnMnist/lswDeepMnist.py) training , 36 images.

![image](https://raw.githubusercontent.com/LinShiwei/TensorflowLearning/master/trainOurOwnMnist/deepMnistTrainingResult.png)
