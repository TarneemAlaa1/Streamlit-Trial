import streamlit as st
st.title('Hello World')
st.header('Header')
st.markdown('markdown')
st.subheader('Subheader')
st.caption('this is caption')
st.code(
'''if x==0 :
    x=2021''')
st.latex(r''' a = a + ar^1 + ar^2 + ar ^3 ''' )

st.markdown("<h1 style = 'text-align : center; color : blue;'> Colorful </h1>", unsafe_allow_html = True)

st.image('https://img.freepik.com/premium-photo/beautiful-gradiant-orange-clouds-sunlight-blue-sky-perfect-background-take-everningtwilight-rainy-seasonwinter-summer_532332-1908.jpg?size=626&ext=jpg&ga=GA1.1.1448711260.1706832000&semt=ais', width = 500, caption = 'Sky')
# st.video()
# st.audio()'

import pandas as pd
df = pd.DataFrame({'k' : [1,2,3,4,5] , 'v' : [1,2,3,4,5]})
st.dataframe(df)
st.table(df)

st.checkbox('Yes')

if st.checkbox('Show DataFrame') :
    st.dataframe(df)

st.button('Click')

# We can store the result in a variable and then be able to anything based on it.
gender  = st.radio('Pick your gender', ['Male', 'female'])

if gender == 'Male' :
    st.write('You are Male')
else : 
    st.write('You are female')

# Drop Down list , but preferrably if we only have two options then a radio button is better.
st.selectbox('Pick your gender', ['Male', 'Female'])


# Multiselect
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Earth', 'Uranus', 'Venus'])

# Slider 
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# Slider for numerical values.
st.slider('Pick a number', 0, 100)
st.slider('Pick a number', 0, 100, step=10)

# Number input
# Only allows numerical values and within the specified range
num1 = st.number_input('Select number 1 within 0-10 ',0,10)
num2 =  st.number_input('Select number 2 within 0-10',0,10)
sum = num1 + num2 
st.write('Result',sum)

# Text input
st.text_input('Email Address')

# Date time picker
st.date_input("Select Date")
st.time_input("Select Time")

st.text_area('Big text area')

st.file_uploader('Upload your image')

st.color_picker("Pick a color")


## Some texts 
st.success("You did it !")

st.error("You failed!")

st.warning('Warning')

st.info('It is easy to build a stream lit app')


## Sidebar
## Anything we previously discussed can be put here.
st.sidebar.title('This is a sidebar')
st.sidebar.header('This is a sidebar header')
st.sidebar.button("Click 2")
st.sidebar.checkbox("This is a checkbox")


## Graphs
##import matplotlib.pyplot as plt
##import numpy as np

##random= np.random.normal(1,2,size = 20)

