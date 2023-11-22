import pymongo
import math
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#icon & detail
st.set_page_config(page_title="Water data TGR_GROUP10",
                    page_icon=":bar_chart:",
                    layout="wide")

st.title("Water Data - TGR GROUP 10")
################################################################################################################

# #pull data from collection.
# @st.cache_data(ttl=600)
# def get_data():
#     db = client.streamlit
#     docs = db.Mypet.find()
#     #print(items)
#     docs = list(docs) #make hashable for st.cache_data
#     return docs

# docs = get_data()

# #Print results.
# for doc in docs:
#     st.write(f"{doc['name']} has a :{doc['weight']}")
MONGO_DETAILS = "mongodb://TGR_GROUP10:LV741N@mongoDB:27017"

@st.cache_resource
def init_connection():
    return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

# pull data from collection.
@st.cache_data(ttl=600)
def get_data():
    db = client.mockupdata
    docs = db.waterdata.find()
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

# ################################################################################################################

# Title for the web app
st.title('Average of Water Data by ...')

# User selects which graph to display
selected_graph = st.selectbox('Select a graph', ['Year', 'Month', 'Date'])
selected_data = st.selectbox('Select a Data to Plot', ['WaterDataFront', 'WaterDataBack', 'WaterDrainRate'])
# Calculate average based on user selection
if selected_graph == 'Year':
    if selected_data == 'WaterDataFront':
        average_data = df.groupby('Year')['WaterDataFront'].mean().reset_index()
        title = 'Average Water Data Front by Year'
    elif selected_data == 'WaterDataBack':
        average_data = df.groupby('Year')['WaterDataBack'].mean().reset_index()
        title = 'Average Water Data Back by Year'
    elif selected_data == 'WaterDrainRate':
        average_data = df.groupby('Year')['WaterDrainRate'].mean().reset_index()
        title = 'Average Water Data Rate by Year'
    
elif selected_graph == 'Month':
    if selected_data == 'WaterDataFront':
        average_data = df.groupby('Month')['WaterDataFront'].mean().reset_index()
        title = 'Average Water Data Front by Year'
    elif selected_data == 'WaterDataBack':
        average_data = df.groupby('Month')['WaterDataBack'].mean().reset_index()
        title = 'Average Water Data Back by Year'
    elif selected_data == 'WaterDrainRate':
        average_data = df.groupby('Month')['WaterDrainRate'].mean().reset_index()
        title = 'Average Water Data Rate by Year'
else:
    if selected_data == 'WaterDataFront':
        average_data = df.groupby('Date')['WaterDataFront'].mean().reset_index()
        title = 'Average Water Data Front by Year'
    elif selected_data == 'WaterDataBack':
        average_data = df.groupby('Date')['WaterDataBack'].mean().reset_index()
        title = 'Average Water Data Back by Year'
    elif selected_data == 'WaterDrainRate':
        average_data = df.groupby('Date')['WaterDrainRate'].mean().reset_index()
        title = 'Average Water Data Rate by Year'

# Plot the bar chart
fig = px.bar(
    average_data,
    x=selected_graph,
    y=selected_data,
    labels={'WaterDataFront': 'Average Water Data Front'},
    title=title
)
# ################################################################################################################

# fig = px.scatter(
#     df.query("year==2007"),
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=True,
#     size_max=60,
# )

# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     # Use the Streamlit theme.
#     # This is the default. So you can also omit the theme argument.
#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# with tab2:
#     # Use the native Plotly theme.
#     st.plotly_chart(fig, theme=None, use_container_width=True)

# ################################################################################################################


# ################################################################################################################


# ################################################################################################################


# Display the plot in Streamlit app
st.plotly_chart(fig)

#Sidebar for the query (Data Frame)
# st.sidebar.header("Select Filters Here:")
# st.header("Filtered")
# city = st.sidebar.selectbox("Select the City:",
#         options=df["Name"].unique(),
#         index=0
# )

# areaLocality = st.sidebar.multiselect("Select Area Locality:",
#         options=df.query("City == @city")["Area_Locality"].unique(),
#         default=df.query("City == @city")["Area_Locality"].unique()[0],
# )

# areaType = st.sidebar.selectbox("Select the Area Type:",
#         options=df["Area_Type"].unique(),
#         index=0
# )

# furnishing = st.sidebar.selectbox("Select the Furnishing Status:",
#         options=df["Furnishing_Status"].unique(),
#         index=0
# )

# df_selection = df.query(
#         "Area_Locality == @areaLocality & Area_Type == @areaType & Furnishing_Status == @furnishing"
# )
# st.dataframe(df_selection) 

# ################################################################################################################

################################################################################################################

# # BAR CHART Average rental
# average_rental_line = df_selection.groupby(by=["Furnishing_Status"]).mean()[["Rent"]]
# #st.dataframe(average_rental_line)
# fig_average_rental = px.bar(
#     average_rental_line,
#     x="Rent",
#     y=average_rental_line.index,
#     orientation="h",
#     title="<b>Average Rental Line</b>",
#     color_discrete_sequence=["#0083B8"] * len(average_rental_line),
#     template="plotly_white",
# )
# #update กรณีข้อฒูลมีการเปลี่ยน มันจะได้เปลี่ยนให้
# fig_average_rental.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )
# scatter_data = df  # Assuming df is your DataFrame

# # Scatter plot
# st.plotly_chart(px.scatter(scatter_data, x='WaterDataFront', y='WaterDataBack',
#                             labels={'WaterDataFront': 'Front Water Level', 'WaterDataBack': 'Back Water Level'},
#                             title='Scatter Plot of WaterDataFront vs WaterDataBack'))

# # Display metrics for the scatter plot
# col1, col2, col3 = st.columns(3)

# # Metrics for WaterDataFront
# col1.metric("Avg WaterDataFront", scatter_data['WaterDataFront'].mean(), delta=scatter_data['WaterDataFront'].diff().mean())

# # Metrics for WaterDataBack
# col2.metric("Avg WaterDataBack", scatter_data['WaterDataBack'].mean(), delta=scatter_data['WaterDataBack'].diff().mean())

# # Additional metric
# col3.metric("Correlation", scatter_data['WaterDataFront'].corr(scatter_data['WaterDataBack']), delta=None)
################################################################################################################
chart_data = df  # Assuming df is your DataFrame
st.title('Latest Water Data')
# Plot line graph
# st.plotly_chart(px.line(chart_data, x='Date', y=['WaterDataFront', 'WaterDataBack', 'WaterDrainRate'],
#                         labels={'value': 'Water Level', 'variable': 'Metrics'},
#                         title='Water Level Metrics Over Time'))

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

# # Scatter plot
# st.plotly_chart(px.scatter(scatter_data, x='WaterDataFront', y='WaterDataBack',
#                             labels={'WaterDataFront': 'Front Water Level', 'WaterDataBack': 'Back Water Level'},
#                             title='Scatter Plot of WaterDataFront vs WaterDataBack'))
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