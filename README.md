# Detection-of-PPE-Compliance-on-Construction-Site-Using-CV
Construction safety is a matter of great concern for practitioners and researchers worldwide. Even after risk assessments have been conducted and adequate controls have been implemented, workers are still subject to safety hazards in construction work environments. The need for personal protective equipment (PPE) is important in this context. Automatic and real-time detection of the non-compliance of workers in using PPE is an important concern. Developments in the field of computer vision and data analytics, especially using deep learning algorithms have the potential to address this challenge in construction. This study developed a framework to sense in real-time, the safety compliance of construction workers with respect to PPE, which is intended to be integrated into the safety workflow of an organization. The study makes use of the Convolutional Neural Networks model, which was developed by applying transfer learning to a base version of the YOLOv3 deep learning network. Taking into account the presence of hardhat and safety jackets, the model predicts compliance in four categories such as NOT SAFE, SAFE, NoHardHat, and NoJacket. A data set of 2,509 images was collected from video recordings from several construction sites and this web-based collection was used to train the model. The model reported an F1 score of 0.96 with an average precision and recall rate at 96% on the test data set. Once a non “SAFE” category is detected by the model, an alarm and a timestamped report are also incorporated to enable a real-time integration and adoption on the construction sites. Overall, the study provides evidence on the feasibility and utility of computer vision-based techniques in automating the safety-related compliance processes at construction sites.

The Project folder is well structured in Google drive. Link : https://drive.google.com/drive/folders/17FcypMej-4hCIJ4112Ahgv5vez4uQi-B?usp=sharing

The weights file is not uploaded due to its large size. You can find it here. https://drive.google.com/file/d/1Yc5kVGvl2T9ThOOR8LpylqCHKD_LBGfJ/view?usp=sharing

The outputs can be found in the below links.

Output Images: https://drive.google.com/drive/folders/1cql4u-uvTi6KDrcnhQ9eplzpqop6QrLE?usp=sharing

Output Videos: https://drive.google.com/drive/folders/11ocbAFf9N6AW9jRrp6fXVqkaTuJfQLg4?usp=sharing
