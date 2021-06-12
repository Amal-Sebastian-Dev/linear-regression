# Imports
import streamlit as st
import pickle

# Load the trained model
with open('lr_sales_predictor.pkl', 'rb') as sales_predictor_file:
    sales_predictor_model = pickle.load(sales_predictor_file)


st.header('Sales Predictor')

# Creating the form
tv_spending = st.text_input('Enter the spending on TV ads:')
radio_spending = st.text_input('Enter the spending on radio ads:')
newspaper_spending = st.text_input('Enter the spending on newspaper ads:')
submit = st.button('Predict')

if submit:
    spending = [[tv_spending, radio_spending, newspaper_spending]]
    predicted_sales = sales_predictor_model.predict(spending)
    st.text('Estimated sales is {}'.format(predicted_sales[0]))