from os import getcwd
from PIL.Image import ROTATE_180
from matplotlib import pyplot
from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
from prophet.serialize import model_from_json
from PIL import Image

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://zupimages.net/up/21/24/qvsm.png");
        background-size: cover
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    
    .big-font {
        font-size:300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_option('deprecation.showPyplotGlobalUse', False)
compagny_list = pd.read_csv('raw_data/compagny.csv')

original_title = '<p style="font-family:Arial; color:white; font-size: 20px;">Pour quelle compagnie voulez vous\n\
obtenir la prédictions des actions ?</p>'
st.sidebar.markdown(original_title, unsafe_allow_html=True)
selected_cmp = st.sidebar.selectbox(label="", options=compagny_list)
original_title = '<p style="font-family:Arial; color:white; font-size: 20px;">Nombre de jours à prédire :'
st.sidebar.markdown(original_title, unsafe_allow_html=True)
nb_jour = st.sidebar.slider(label="", min_value=2, max_value=28)



if st.sidebar.button('Go !'):
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    path = f'models/{selected_cmp}_model.json'
    
    with open(path, 'r') as fin:
        model = model_from_json(json.load(fin))  # Load model
    
    jours = 6 + int(nb_jour)
        
    X_pred = model.make_future_dataframe(periods=jours, freq='D', include_history=False)
    
    results = model.predict(X_pred)
    results = results.iloc[6:]
    
    fig, ax = plt.subplots()
    ax.patch.set_facecolor('grey')
    ax.patch.set_alpha(0.5)
    ax.plot(results['ds'],results['yhat'])
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
    ax.set_xticks(results['ds'])
    plt.ylabel('Dollars', size=20)
    plt.xlabel('Date', size=20)
    
    if selected_cmp == 'FB':
        titre = 'Facebook'
    elif selected_cmp == 'GOOG':
        titre = 'Google'
    elif selected_cmp == 'AMZN':
        titre = 'Amazon'
    elif selected_cmp == 'MSFT':
        titre = 'Microsoft'
    elif selected_cmp == 'AAPL':
        titre = 'Apple'
    elif selected_cmp == 'GS':
        titre = 'Golman Sachs'
    elif selected_cmp == 'JPM':
        titre = 'JPMorgan'
    elif selected_cmp == 'BAC':
        titre = 'Bank of America'
    elif selected_cmp == 'WFC':
        titre = 'Wells Fargo & Compagny'
    elif selected_cmp == 'CG':
        titre = 'The Carlyle Group'
        
    plt.title(titre + ' prévision à ' + str(nb_jour) + ' jours', size = 20)
    st.pyplot()
    
    if results.iloc[:1]['yhat'].values[0] < results.iloc[-1:]['yhat'].values[0] :
        image = Image.open('soleil.png')
        st.sidebar.image(image, caption="Il va faire beau, c'est le moment d'acheter !", output_format='png')
    else:
        image = Image.open('pluie.png')
        st.sidebar.image(image, caption="Il va pleuvoir, c'est le moment de vendre !", output_format='png')
