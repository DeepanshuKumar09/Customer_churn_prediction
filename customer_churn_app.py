
import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle

# 1. Load the pre-trained Keras model
model = load_model('churn_model.h5')

# 2. Load the StandardScaler object
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# 3. Set the title of the Streamlit application
st.title('Customer Churn Prediction')
st.write('Enter customer details to predict if they will churn.')

# 4. Create input widgets for each of the 11 features
# Organize inputs into columns for better layout

col1, col2, col3 = st.columns(3)

with col1:
    CreditScore = st.number_input('Credit Score', min_value=350, max_value=850, value=650)
    Age = st.slider('Age', min_value=18, max_value=92, value=35)
    Tenure = st.slider('Tenure (years)', min_value=0, max_value=10, value=5)
    Balance = st.number_input('Balance', min_value=0.0, value=50000.0, format='%.2f')

with col2:
    NumOfProducts = st.radio('Number of Products', options=[1, 2, 3, 4], index=1)
    HasCrCard = st.radio('Has Credit Card?', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    IsActiveMember = st.radio('Is Active Member?', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    EstimatedSalary = st.number_input('Estimated Salary', min_value=0.0, value=75000.0, format='%.2f')

with col3:
    Geography_Germany = st.radio('Geography: Germany?', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    Geography_Spain = st.radio('Geography: Spain?', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    Gender_Male = st.radio('Gender: Male?', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

# 5. Create a 'Predict' button
if st.button('Predict Churn'):
    # Collect all user inputs into a pandas DataFrame
    user_input = pd.DataFrame([[CreditScore, Age, Tenure, Balance, NumOfProducts,
                                HasCrCard, IsActiveMember, EstimatedSalary,
                                Geography_Germany, Geography_Spain, Gender_Male]],
                               columns=['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                                        'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
                                        'Geography_Germany', 'Geography_Spain', 'Gender_Male'])

    # Scale the user input
    # All features are expected to be scaled based on how X_train_trf was generated
    scaled_input = scaler.transform(user_input)

    # Make a prediction using the loaded Keras model
    prediction_probability = model.predict(scaled_input)[0][0]

    # Display the prediction
    if prediction_probability >= 0.5:
        st.error(f'The customer is likely to churn. Probability: {prediction_probability:.2f}')
    else:
        st.success(f'The customer is not likely to churn. Probability: {prediction_probability:.2f}')


