# Diabetes Prediction Web Application



https://github.com/user-attachments/assets/3200c096-3f2d-424b-9757-db4ae70021ed



![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)

A machine learning web application that predicts diabetes using SVM.

## Dataset (kaggle)

https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv



## Project Overview
This project implements a complete ML pipeline:
1. Trains a Support Vector Machine (SVM) classifier with PCA dimensionality reduction
2. Optimizes model hyperparameters using grid search
3. Builds a preprocessing pipeline for feature scaling
4. web application using Flask

Key components:
- **ML Pipeline**: PCA + SVM with optimized hyperparameters
- **Preprocessing**: Standard scaling and feature engineering
- **Web Interface**: HTML form for input collection
