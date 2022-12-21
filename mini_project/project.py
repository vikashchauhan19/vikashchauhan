# 1. import libraries
import numpy as np
import pandas as pd
import plotly.express as px # simple graphs
import plotly.graph_objects as go # complex graphs
import streamlit as st


st.set_page_config(layout='wide')
# common varibales
years = list(range(1890,2022))



def clean_dataset(df):
    df.drop(columns=['overview','original_title'], axis=1, inplace= True)    
    df.release_date = pd.to_datetime(df.release_date)
    df.rename(mapper={'original_language':'language'}, axis=1, inplace=True)                             
    return df



# 3. creat function to clean data
st.cache()                                                       
def load_dataset():
    df= pd.read_csv('data/movies_datasets.csv')
    df = clean_dataset(df)
    return df

st.title("Movies released from 1890-2022")
with st.spinner("loading dataset"):                               
    df= load_dataset()
    #st.balloons()


if st.sidebar.checkbox('show full dataframe'):                 
    st.write(df,use_container_width=True)

st.sidebar.header("Select the year visualize")
years = df.release_date.dt.year.unique().tolist()
yr = st.sidebar.selectbox("Years", years)
st.sidebar.header("Select the movie rating visualize")
rating = np.arange(1,10)
rtg = st.sidebar.selectbox("Rating", rating)
st.sidebar.header("Select the Language visualize")
Language = df.language.unique().tolist()
lang = st.sidebar.selectbox("language ", Language)

#graph

filter1 = df.release_date.dt.year == yr
filter2 = (df.vote_average >= rtg )& (df.vote_average < rtg+1 )
filter3 = df.language == lang
subset = df[filter1 & filter2 & filter3].copy()
st.dataframe(subset, use_container_width=True)


fig = px.line(df.sort_values('popularity').head(100), x='popularity', )
st.plotly_chart(fig, use_container_width=True)




# # 6.give user option displaY graphs0
# # 0.Run the app run the command below 
# #  streamlit run project.py