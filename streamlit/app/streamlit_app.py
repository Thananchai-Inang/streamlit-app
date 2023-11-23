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
    docs = db.waters_collection.find()

    #water test - genmock
    # docs = db.genmockdata.find()

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

# Using object notation
selected_data = st.sidebar.selectbox(
    "Select data to plot",
    ("waterlevel", "waterdrain")
)

# Line plot
st.line_chart(df[selected_data])

#################################################################################################################


# Sort DataFrame by date in descending order
df = df.sort_values(by='day', ascending=False)

# Get the latest row
latest_row = df.iloc[0]

# Display the latest values in a Streamlit metric
st.sidebar.metric(label='Latest Water Level', value=latest_row['waterlevel'], delta=None)
st.sidebar.metric(label='Latest Water Drain', value=latest_row['waterdrain'], delta=None)



#################################################################################################################


#################################################################################################################


#################################################################################################################


#################################################################################################################


################################################################################################################


################################################################################################################
