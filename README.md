# Introduction
![sign-language-model-intro-2](https://github.com/IremOztimur/Turkish-Sign-Language-Detector/assets/77894816/7d58cb3e-6964-4863-ad77-fd2006149b2d)

## 1. Gather and Label Training Images
This step is crucial for ensuring the accuracy of the model. The training images should feature random objects alongside the desired ones, and they should encompass a diverse range of backgrounds and lighting conditions. For this project, each label will consist of 50 different images. With four distinct Turkish Sign Language words in mind, I will gather a total of 200 images and label them using [LabelImg](https://github.com/HumanSignal/labelImg).

- [TO-DO] Put images

## 2. Install TensorFlow Object Detection Dependencies
I chose to install the TensorFlow Object Detection API in Google Colab for its convenience. This involves cloning the TensorFlow models [repository](https://github.com/tensorflow/models) and executing a couple of installation commands. You can access the code segment in the Google Colab instance where I trained the model.
