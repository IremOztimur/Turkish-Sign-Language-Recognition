# Introduction
![sign-language-model-intro-2](https://github.com/IremOztimur/Turkish-Sign-Language-Detector/assets/77894816/7d58cb3e-6964-4863-ad77-fd2006149b2d)

## 1. Gather and Label Training Images
This step is crucial for ensuring the accuracy of the model. The training images should feature random objects alongside the desired ones, and they should encompass a diverse range of backgrounds and lighting conditions. For this project, each label will consist of 50 different images. With four distinct Turkish Sign Language words in mind, I will gather a total of 200 images and label them using [LabelImg](https://github.com/HumanSignal/labelImg).

<img width="932" alt="images-file-structure" src="https://github.com/IremOztimur/Turkish-Sign-Language-Detector/assets/77894816/4eeea2ed-30dc-4151-80ee-ace41b8d034e">


## 2. Install TensorFlow Object Detection Dependencies
I chose to install the TensorFlow Object Detection API in Google Colab for its convenience. This involves cloning the TensorFlow models [repository](https://github.com/tensorflow/models) and executing a couple of installation commands. You can access the code segment in the Google Colab instance where I trained the model.

## 3. Upload Image Dataset and Prepare Training Data
We'll upload our images, split them into train, validation, and test folders, and then run scripts for creating TFRecords from our data.
First, on your local PC, zip all your training images and XML files into a single folder called "images.zip". The files should be directly inside the zip folder, or in a nested folder as shown below:

images.zip
-- images
  -- img1.jpg
  -- img1.xml
  -- img2.jpg
  -- img2.xml
  ...

## 4. Set Up Training Configuration
In this section, we'll set up the model and training configuration. We'll specifiy which pretrained TensorFlow model we want to use from the TensorFlow 2 Object Detection Model Zoo. For this project I used [http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz]
