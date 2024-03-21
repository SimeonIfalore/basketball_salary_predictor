import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open("nba_model",'rb'))

st.title('Basketball salary predictor')
st.sidebar.header('Player Data')
player_image = Image.open("pexels-rdne-stock-project-7005234.jpg")
st.image(player_image,width=550)

#creating a function for the values
def user_report():
    rating = st.sidebar.number_input('Player rating', 0,100)
    geo = st.sidebar.selectbox('please select Country', ('USA','Canada','Australia','Others'))
    if(geo == 'USA'):
        country = 0
    elif(geo == 'Canada'):
        country = 1
    elif(geo == 'Australia'):
        country = 2
    else:
        country = 3
    draft_year = st.sidebar.slider('Draft  year', 2000, 2050)
    draft_round = st.sidebar.slider('Draft  round', 1, 20)
    draft_peak = st.sidebar.slider('Draft  peak', 1, 50)
    Age = st.sidebar.number_input('Player Age', 0,100)

    # creating a dictionary of the values
    user_report_data = {
        'rating': rating ,
        'country': country,
        'draft_year': draft_year,
        'draft_round': draft_round,
        'draft_peak': draft_peak,
        'Age': Age
    }
    report_data = pd.DataFrame(user_report_data, index = [0])
    return report_data
user_data = user_report()

st.subheader('Player data summary')
st.write(user_data)

salary = model.predict(user_data)

st.subheader('Player salary')
st.subheader('$' + str(np.round(salary[0])))
