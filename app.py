import streamlit as st
import pandas as pd


'''
# Welcome to MeteoStocks
'''

'''

'''
compagny_list = pd.read_csv('raw_data/compagny.csv')

st.sidebar.text("Pour quelle compagnie voulez vous\n\
obtenir la prédictions des actions ?")
selected_cmp = st.sidebar.selectbox(label="", options=compagny_list)



url = ''

parameters = {
    'compagny':selected_cmp,
}

'''
Call API
'''

'''
Retrieve the prediction from the **JSON** returned by the API...
'''
