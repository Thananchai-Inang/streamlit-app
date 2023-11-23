import pymongo
import math
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt


#icon & detail
st.set_page_config(page_title="Water data TGR_GROUP10",
                    page_icon=":bar_chart:",
                    layout="wide")

st.title("Water Data - TGR GROUP 10")
################################################################################################################

MONGO_DETAILS = "mongodb://TGR_GROUP10:LV741N@mongoDB:27017"

@st.cache_resource
def init_connection():
    return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

# pull data from collection.
@st.cache_data(ttl=0)
def get_data():
    db = client.water_data
    # # water real
    # docs = db.waters_collection.find()
    #water test - genmock
    docs =db.genmockdata.find()
    # print(items)
    docs = list(docs)  # make hashable for st.cache_data
    return docs

docs = get_data()

# Convert data to a DataFrame
df = pd.DataFrame(docs)


################################################################################################################

# st.header("Raw Data")

# Boolean variable to track the visibility of content
show_content = st.checkbox('Show/Hide raw data')

# Display content based on the visibility state
if show_content:
    st.write(df)


#################################################################################################################
st.header('Plot the data over days')

# Selectbox for choosing data type
water_list = ['waterlevel', 'waterdrain']
selected_data = st.selectbox('Select a data to plot:', water_list)

# Line plot
st.line_chart(df[selected_data])

#################################################################################################################


#################################################################################################################


#################################################################################################################


#################################################################################################################


#################################################################################################################


################################################################################################################


################################################################################################################
