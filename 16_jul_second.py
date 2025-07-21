# importing all libraries
import streamlit as st
import pandas as pd
import numpy as np


st.title('My first streamlit app')  # st.tilte shows the title on the page
st.write('This app shows the basic functionalities of streamlit') # st.write is used to display text on the page

#creating a sidebar for user input
st.sidebar.header('User Input Features')  # sidebar header

user_name=st.sidebar.text_input('Enter your Name')  # text input for user name sidebar.textinput is for input i sidebar
age=st.sidebar.slider("Your age")   # slider for age
fav_color=st.sidebar.selectbox('Your favorite colour:',['Blue','Red','Green','Yellow']) # select box for favourite color

# Displaying the user input
st.header(f'Welcom,{user_name}')
st.write(f'{user_name},you are {age} years old')
st.write(f'{user_name},your favourite colour is {fav_color}')

#Generating and displaying a random dataframe
st.subheader('Random Dataframe')
data=pd.DataFrame(
    np.random.randn(10,5),   # created a dataframe with 10 rows and 5 columns
    columns=("cpl %d " % i for i in range(5)), # column names are cpl 0 to cpl 4
)
st.dataframe(data)   # displaying the dataframe