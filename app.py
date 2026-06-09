import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from powerbi import powerbi_dashboard
st.set_page_config(
    page_title="Ola_ride",
    layout="wide"
)


st.title("Ola Ride Dashboard")


df=pd.read_csv("ola_dataset.csv")

col1,col2,col3=st.columns(3)
col1.metric(
    "Total Ride",
    len(df)
)
col2.metric(
    "Revenue",
    f"{df['Booking_Value'].sum():,.0f}"
)


col3.metric(
    "Avg Customer Rating",
    
    round(df["Customer_Rating"].mean(),2)
)

st.sidebar.header("Filters")
Vehicle=st.sidebar.selectbox(
    "Vehicle_Type",
    ["All"]+list(df["Vehicle_Type"].unique())
)
if Vehicle != "All":
    df = df[df["Vehicle_Type"] == Vehicle]

st.subheader("Dataset Preview")
st.dataframe(df)

search=st.text_input(
    "Enter customer id:"
)
if search:
    result=df[df["Customer_ID"].astype(str).str.contains(search)]
    st.dataframe(result)
query=st.selectbox(
    "select query",
    [
       "successful bookings",
       "average ride distance per vehicle type",
       "total number of cancelled rides by customers",
       "List the top 5 customers who booked the highest number of rides",
       "the number of rides cancelled by drivers due to personal and car-related issues",
       "the maximum and minimum driver ratings for Prime Sedan bookings",
       "Retrieve payment mode using UPI",
       "average customer rating per vehicle type",
       "Calculate the total booking value of rides completed successfully",
       "List all incomplete rides along with the reason"
    ]
)
if query=="successful bookings":
    result=df[df["Booking_Status"]=="Success"]
    st.dataframe(result)

if query=="average ride distance per vehicle type":
    result=round(df.groupby("Vehicle_Type")["Ride_Distance"].mean().reset_index(),2)
    st.dataframe(result)

if query=="total number of cancelled rides by customers":
    result=df[df["Booking_Status"]=="Canceled by Customer"]
    st.write("total number of cancelled rides:", len(result))

if query=="List the top 5 customers who booked the highest number of rides":
    result=(df.groupby("Customer_ID").size().reset_index(name="Total_rides").sort_values(by="Total_rides", ascending=False).head(5))
    st.dataframe(result)

if query=="the number of rides cancelled by drivers due to personal and car-related issues":
    result=df[df["Canceled_Rides_by_Driver"]=="Personal & Car related issue"]
    st.dataframe(result)

if query=="the maximum and minimum driver ratings for Prime Sedan bookings":
    result=(df[df["Vehicle_Type"]=="Prime Sedan"])
    st.write("the maximum driver ratings for Prime Sedan booking:", result["Driver_Ratings"].max())
    st.write("the minimum driver ratings for Prime Sedan booking:", result["Driver_Ratings"].min())


if query=="Retrieve payment mode using UPI":
    result=df[df["Payment_Method"]=="UPI"]
    st.dataframe(result)

if query=="average customer rating per vehicle type":
    result=round(df.groupby("Vehicle_Type")["Customer_Rating"].mean(),2)
    st.dataframe(result)

if query=="Calculate the total booking value of rides completed successfully":
    result=(df[df["Incomplete_Rides"]=="No"]["Booking_Value"].sum())
    st.write("the total completed rides are:",result)


if query=="List all incomplete rides along with the reason":
    result=df[df["Incomplete_Rides"]=="Yes"]
    st.dataframe(result)


powerbi_dashboard(df)    