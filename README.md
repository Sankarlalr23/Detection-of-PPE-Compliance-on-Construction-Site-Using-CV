# Detection-of-PPE-Compliance-on-Construction-Site-Using-CV

## 1.	INTRODUCTION

All over the world, construction is one of the most hazardous industries due to its unique nature. Construction safety is always a matter of concern for both practitioners and researchers. The number of fatal injury accidents reported every year is very high in construction industry. Even after sufficient risk assessments and the implementation of adequate controls in the work environment, workers could still be subject to health and safety risks from hazards, which is why Personal Protective Equipment (PPE) is important.

Every week, a huge amount of pictures and videos are being captured on projects around the world, with many of them being used to track progress, resolve claims, identify quality issues, etc. Safety is of highest priority in construction, as per the OSHA report approximately 1 in 10 workers injured on the job site each year. It is not practically possible for dedicated safety experts to visit every site. But what if there was a way for these computer vision engines to review images and predict the level of safety in the site.

This paper gives a model to detect people wearing PPE namely hardhat and safety jacket, save image instances and generate date wise report of those who are not wearing both. The model is created by applying transfer learning to YOLOv3 network.

## 2.	FEATURES OF YOLOV3

Transfer learning is applied to YOLOv3 to create the model; hence the basic network features remains the same. 

YOLOv3 is a recent object classifier network, released on April 2018. YOLOv3 has a Frames Per Second (FPS) rate and Execution time of 35 and 29 milliseconds respectively on COCO dataset as shown in figure 1, mAP-50 is 55.3 for the same [1]. Another important feature is that YOLOv3 makes predictions at three different scales [1]. The predictions for the third scale benefit from all the prior computations as well as fine-grained features from early on in the network [1]. YOLOv3 performs very well in the fast detector category when speed is important [2]. When accuracy vs speed is plotted on the AP50 metric, YOLOv3 has significant benefits over other detection systems. Namely, faster and better [1]. For the same reason, this network is used, as we are dealing with real time detection of people wearing PPE on construction site. 

![image](https://user-images.githubusercontent.com/68675380/118487749-a806c680-b738-11eb-91c5-af6b974ccb53.png)

## 3.	EXPERIMENTAL METHOD  



The Project folder is well structured in Google drive. Link : https://drive.google.com/drive/folders/17FcypMej-4hCIJ4112Ahgv5vez4uQi-B?usp=sharing

The weights file is not uploaded due to its large size. You can find it here. https://drive.google.com/file/d/1Yc5kVGvl2T9ThOOR8LpylqCHKD_LBGfJ/view?usp=sharing

# The outputs can be found in the below links.

Output Images: https://drive.google.com/drive/folders/1cql4u-uvTi6KDrcnhQ9eplzpqop6QrLE?usp=sharing

Output Videos: https://drive.google.com/drive/folders/11ocbAFf9N6AW9jRrp6fXVqkaTuJfQLg4?usp=sharing
