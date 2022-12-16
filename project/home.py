# 1. import libraries
import numpy as np
import pandas as pd
import plotly.express as px # simple graphs
import plotly.graph_objects as go # complex graphs
import streamlit as st
# common varibales
years = list(range(1980,2014))


# 2. creat function to load data
def clean_dataset(df):
    df.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace= True)     # drop columns
    df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region', 'DevName':'Status'}, inplace=True) # rename column
    # st.write(df.columns)
    df.set_index('Country',inplace = True)                       # set country as index
    df['Total'] = df[years].sum(axis=1)                          # add a total column to the data frame
    return df



# 3. creat function to clean data
st.cache()                                                       # helps to make the app faster
def load_dataset():
    df= pd.read_excel('data/Canada.xlsx',sheet_name='Canada by Citizenship', skiprows=20, skipfooter= 2)
    df = clean_dataset(df)
    return df
# 4. setup basic UI
st.title("Immigration from Countries to Canada")
with st.spinner("loading dataset"):                               #show a loading message
    df= load_dataset()
    #st.balloons()


if st.sidebar. checkbox('show full dataframe'):                   # show raw data if checkbox is checked
    st.write(df)

#5.give user options  to select coulumns
st.sidebar.header("Select the country visualize")
countries = df.index.tolist()
sel_country = st.sidebar.selectbox("Country", countries)

 #graph

st.header(f'Immigration from {sel_country} to Canda')
country = df.loc[sel_country ,  years] # subset
fig = px.line(country, x = country.index, y=country.values)
st.plotly_chart(fig)


st.sidebar.header("Select multiple Countries to visualize")
sel_countries = st.sidebar.multiselect("Countries",countries)
if len(sel_countries)>1:
    st.header(f'Comparing countries{",".join(sel_countries)}')
    df_countries = df.loc[sel_countries,years].T                      # subset
    fig = px.bar(df_countries, x=years, y = sel_countries)
    st.plotly_chart(fig)
else:
    st.warning('Please select at least 2 countries for comparison')    


# 6.give user option displaY graphs0
# 0.Run the app run the command below 
#  streamlit run home.py