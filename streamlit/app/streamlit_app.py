import pymongo
import math
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#icon & detail
st.set_page_config(page_title="House Rent Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide")
################################################################################################################

MONGO_DETAILS = "mongodb://TGR_GROUP10:LV741N@mongoDB:27017"
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

#pull data from collection.
@st.cache_data(ttl=600)
def get_data():
    db = client.streamlit
    docs = db.Mypet.find()
    #print(items)
    docs = list(docs) #make hashable for st.cache_data
    return docs

docs = get_data()

#Print results.
for doc in docs:
    st.write(f"{doc['name']} has a :{doc['weight']}")


st.title("House Rent Dataset - TGR GROUP 10")

st.header("Dataset for the Exploration")
#import csv
# df = pd.read_csv('House_Rent_Dataset.csv')
# st.dataframe(df)

# ################################################################################################################

# #Sidebar for the query (Data Frame)
# st.sidebar.header("Select Filters Here:")
# st.header("Filtered")
# city = st.sidebar.selectbox("Select the City:",
#         options=df["City"].unique(),
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
# # ---- MAINPAGE ----
# st.title(":bar_chart: House Rent Dashboard")
# st.markdown("##")

# average_rent = round(df_selection["Rent"].mean(),1)
# average_size = round(df_selection["Size"].mean(), 2)
# left_column, right_column = st.columns(2)
# with left_column:
#     st.subheader("Average Rentalt:")
#     st.subheader(f"US $ {average_rent:,}")
# with right_column:
#     st.subheader("Average Size Room:")
#     st.subheader(f"M {average_size}")

# st.markdown("""---""")

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

################################################################################################################

