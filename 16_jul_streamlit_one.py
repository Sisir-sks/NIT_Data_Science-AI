import streamlit as st
st.title('My first streamlit app created by Sisir')
st.write("Welcome! This app calculates the squre of number")

st.header('select a number')
number=st.slider('Pick a number ',0,100,25)   # used slider to select a number

#calculating the result
st.header('Result')
result=number**2
st.write(f'The squre of {number} is {result}.')