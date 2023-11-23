import pymongo
import math
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


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

st.header("Raw Data")

# Convert data to a DataFrame
df = pd.DataFrame(docs)

# Print results using DataFrame
st.write(df)

################################################################################################################
#plot for cleaning

st.header("Let's Explore and Plot the Raw Data!!")

# Filter columns excluding '_id'
columns_to_plot = [col for col in df.columns if col != '_id']

# Choose the column to plot
column_to_plot = st.selectbox("Select a column to plot:", columns_to_plot)

# Bar chart with a title
st.bar_chart(df[[column_to_plot]].rename(columns={column_to_plot: 'Selected Column'}))

#################################################################################################################

# Create a scatter plot using Matplotlib
fig, ax = plt.subplots()
ax.scatter(df['x'], df['y'])

# Set the x-axis range as per your requirement
ax.set_xlim(80, 100)

# Display the plot using Streamlit
st.pyplot(fig)

# st.scatter_chart(df["waterlevel"])

#################################################################################################################


#################################################################################################################


#################################################################################################################


#################################################################################################################


#################################################################################################################


################################################################################################################


################################################################################################################
chart_data = df  # Assuming df is your DataFrame
st.title('Latest Water Data')

# Display metrics
col1, col2 = st.columns(2)

# Metrics for WaterDataFront
col1.metric("WaterDataFront", df['WaterDataFront'].iloc[-1], delta=df['WaterDataFront'].diff().iloc[-1])

# Metrics for WaterDataBack
col2.metric("WaterDataBack", df['WaterDataBack'].iloc[-1], delta=df['WaterDataBack'].diff().iloc[-1])

# Additional metrics for WaterDrainRate
st.metric("WaterDrainRate", df['WaterDrainRate'].iloc[-1], delta=df['WaterDrainRate'].diff().iloc[-1])


################################################################################################################

scatter_data = df  # Assuming df is your DataFrame


st.title('Average Water Data Front and Back Metrics')
# Display metrics for the scatter plot
col1, col2 = st.columns(2)


# Metrics for WaterDataFront
col1.metric("Avg WaterDataFront", scatter_data['WaterDataFront'].mean(), delta=scatter_data['WaterDataFront'].diff().mean())

# Metrics for WaterDataBack
col2.metric("Avg WaterDataBack", scatter_data['WaterDataBack'].mean(), delta=scatter_data['WaterDataBack'].diff().mean())










#correlation
# Group by 'Year' and calculate the average of 'WaterDataBack'
average_water_data_back = df.groupby('Year')['WaterDataBack'].mean().reset_index()

# Streamlit app
st.title('Year and Average WaterDataBack Correlation')

# Line plot using Plotly Express
fig = px.line(average_water_data_back, x='Year', y='WaterDataBack', labels={'WaterDataBack': 'Average Water Data Back'})
fig.update_layout(title='Correlation between Year and Average WaterDataBack',
                  xaxis_title='Year',
                  yaxis_title='Average Water Data Back')

# Display the plot in Streamlit app
st.plotly_chart(fig)


# Group by 'Month' and calculate the average of 'WaterDataBack'
average_water_data_back_monthly = df.groupby('Month')['WaterDataBack'].mean().reset_index()

# Streamlit app
st.title('Month and Average WaterDataBack Correlation')

# Line plot using Plotly Express
fig_monthly = px.line(average_water_data_back_monthly, x='Month', y='WaterDataBack', labels={'WaterDataBack': 'Average Water Data Back'})
fig_monthly.update_layout(title='Correlation between Month and Average WaterDataBack',
                          xaxis_title='Month',
                          yaxis_title='Average Water Data Back')

# Display the plot in Streamlit app
st.plotly_chart(fig_monthly)






#correlations
# Streamlit app
st.title('Correlation between Water Data Columns')

# Select the relevant columns for correlation
selected_columns = ['WaterDataFront', 'WaterDataBack', 'WaterDrainRate']

# Scatter matrix using Plotly Express
fig_scatter_matrix = px.scatter_matrix(df[selected_columns], dimensions=selected_columns,
                                      labels={col: col for col in selected_columns},
                                      title='Correlation Between Water Data Columns')

# Display the plot in Streamlit app
st.plotly_chart(fig_scatter_matrix)