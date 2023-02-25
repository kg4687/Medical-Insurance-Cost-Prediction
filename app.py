"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import numpy as np
import streamlit as st
#load the model
loaded_model = pickle.load(open("Medical_Insurance_trained_model.sav",'rb'))
def medical_insurance_prediction(input_data):
    input_data = (21,1,25.745,0,1,2)
    input_data_array = np.asarray(input_data)

    input_data_reshaped = input_data_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print('the Charges will be : ')
    print(prediction)
    return pridiction 

    
def main():
    st.title("Medical Insurance Prediction")
    age = st.text_input('Age :')
    sex = st.text_input('Sex :(1->Male, 0->Female)')
    bmi = st.text_input('Enter your BMI :')
    smoker = st.text_input('Smoker : (1->Yes, 0->No)')
    region = st.text_input('Region :(3-> Southwest,2->Southeast,1->Northeast, 0->Northwest)')
    children = st.text_input('Enter no. of your children')
    #available for prediction
    charges = ''
    if st.button('Medical Insurance Charge:'):
        charges = medical_insurance_prediction([age,sex,bmi,smoker,region,children])
   
    st.success(charges)
if __name__ == '__main__':
    main()
