# Breast-Cancer-Classification
Breast Cancer Prediction using Logistic Regression
This repository contains a simple implementation of a breast cancer prediction model using Logistic Regression. The dataset used is the Breast Cancer Wisconsin dataset, which is a part of the sklearn.datasets module.

Introduction
Breast cancer is one of the most common types of cancer in women. Early detection and treatment are crucial for improving survival rates. Machine learning techniques, such as logistic regression, can assist in predicting the presence of breast cancer based on various medical measurements.

Dataset
The Breast Cancer Wisconsin dataset contains 569 samples of malignant and benign tumor cells. Each sample has 30 features, including:
id	
diagnosis	
radius_mean	
texture_mean	
perimeter_mean	
area_mean	
smoothness_mean	
compactness_mean	
concavity_mean	
concave points_mean	
symmetry_mean	
fractal_dimension_mean	
radius_se	texture_se	
perimeter_se	
area_se	
smoothness_se	
compactness_se	
concavity_se	
concave points_se	
symmetry_se	
fractal_dimension_se	
radius_worst	
texture_worst	
perimeter_worst	
area_worst	
smoothness_worst	
compactness_worst	
concavity_worst	
concave points_worst	
symmetry_worst	
fractal_dimension_worst

The target variable (label) indicates whether the tumor is malignant (0) or benign (1).

Necessary libraries used are as follows:
numpy and pandas for data manipulation.
sklearn.datasets for loading the dataset.
train_test_split from sklearn.model_selection for splitting the data.
LogisticRegression from sklearn.linear_model for building the model.
accuracy_score from sklearn.metrics for evaluating the model.


Conclusion:
This simple implementation demonstrates how to use logistic regression to predict breast cancer using the Breast Cancer Wisconsin dataset. The model achieved an accuracy of approximately 95% on the test data, showing promising results.

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments:
The Breast Cancer Wisconsin dataset is available from the UCI Machine Learning Repository.
The sklearn library provides excellent tools for machine learning.
