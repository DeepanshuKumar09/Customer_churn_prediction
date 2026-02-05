<div align="center">

# 🔮 Customer Churn Prediction App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)

**A deep learning-powered tool to predict customer attrition and enable proactive retention strategies.**

[View Demo](#) · [Report Bug](#) · [Request Feature](#)

</div>

---

## 📖 Project Overview

Customer churn is a critical metric for businesses, representing the rate at which customers stop doing business with a company. This project leverages a pre-trained **Artificial Neural Network (ANN)** to predict the likelihood of a customer leaving based on their demographic and financial attributes.

The application serves as a bridge between complex machine learning models and end-users, offering a simple, interactive interface for real-time predictions.

---

## 🚀 Key Components

| Component | Description |
| :--- | :--- |
| **🧠 Neural Network** | A sequential Keras model (`churn_model.h5`) optimized for binary classification. |
| **⚖️ Data Scaler** | A `StandardScaler` (`scaler.pkl`) ensuring input data matches training distribution. |
| **💻 Streamlit UI** | An interactive web dashboard (`app.py`) for real-time user input and visualization. |

---

## 🛠️ Features & Inputs

The model analyzes **11 key indicators** to generate a prediction. These features are categorized below:

<div align="center">

| 📊 Financial Data | 👤 Demographics | 🌍 Geography & Status |
| :--- | :--- | :--- |
| `CreditScore` | `Age` | `Geography` (Germany/Spain/France) |
| `Balance` | `Gender` | `IsActiveMember` |
| `EstimatedSalary` | `Tenure` | `HasCrCard` |
| `NumOfProducts` | | |

</div>

