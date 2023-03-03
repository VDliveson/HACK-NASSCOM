import streamlit as st
import pandas as pd
import numpy as np
import os

st.title('Heatwave prediction for Telangana')

@st.cache_data
def load_data():
    data = pd.read_csv(r"complete_merged.csv",index_col= 0)
    data['date'] = pd.to_datetime(data['date'])
    return data


data_load_state = st.text('Loading data...')
data = load_data()

# districts = data['district'].unique()
# Notify the reader that the data was successfully loaded.

district_list = [ 'Adilabad', 'Nizamabad', 'Warangal', 'Karimnagar','Khammam' ]
for district in district_list:
    district_data = data.loc[data['district']==district]
    temp = district_data['temp_max']
    dates = district_data['date']
    df = pd.DataFrame({'date':dates,'temp_max':temp})
    df = df.set_index('date')
    st.subheader('Chart for district {}'.format(district))
    st.line_chart(df)

st.subheader('Raw data')
st.write(data)

st.subheader('All data districts')
st.write(district_list)
