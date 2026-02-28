# Skin Cancer Detection Using CNN

This project aims to detect melanoma, a type of skin cancer, using Convolutional Neural Networks (CNN). The model is trained on the HAM10000 dataset, which contains images of localized skin cells. It predicts whether a tumor in the input image is benign or malignant with an accuracy of approximately 90%.

## Dataset
The HAM10000 dataset consists of 10000 dermatoscopic images. Each image is labeled with either 'Benign' or 'Malignant' class. If the given input image lies in 'Benign' class then the cells are non-cancerous else they are cancerous.

## Technologies Used
- flask
- flask-cors
- tensorflow-cpu
- numpy
- Pillow
- gunicorn
 

## Model Architecture
The Convolutional Neural Network (CNN) architecture used for this project consists of multiple convolutional layers followed by max-pooling layers for feature extraction. The extracted features are then passed through fully connected layers for classification. The model is trained using the HAM10000 dataset with appropriate data augmentation techniques to improve generalization.

## Deployment
<img width="1273" height="665" alt="image" src="https://github.com/user-attachments/assets/e0cbf1e9-0efe-46d8-b9e4-4225ea04871e" />
<img width="1299" height="698" alt="image" src="https://github.com/user-attachments/assets/00a1c3df-06d7-4235-a531-9700b125683c" />
Link-https://sentinellessionai.lovable.app/
