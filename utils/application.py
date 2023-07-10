import numpy as np
import pandas as pd 
import streamlit as st
from utils.config_reader import config_reader 
#from models.models_collection import ModelRandomForest
#import pickle
#import os
#from sklearn import preprocessing  
#from sklearn.model_selection import train_test_split 
#import json

# Import of parameters
config = config_reader('config/config.json')

# # loading saved model
# with open(os.path.join(config.model_path, 'model_rf.pkl'), 'rb') as f:
#     model = pickle.load(f)
    


st.write("""
# This app predicts hotel rating!
""")


st.sidebar.header('User Input Parameters')

# This downloads data

#df_train = pd.read_csv(config.data_dir[1:] + 'hotels.zip') # train
#df_test = pd.read_csv(config.data_dir[1:] + 'hotels_test.zip') # test
df_train = pd.read_csv('./data/hotels.zip', index_col=0) # train
st.dataframe(df_train)  # Same as st.write(df)


#data = pd.read_csv('df_sample_data.csv', index_col=0) 

#st.dataframe(df)  # Same as st.write(df)

#selected_indices = st.multiselect('Select rows:', df.index)