import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def powerbi_dashboard(df):
    

    st.title("Analytic Dasboard")




    query=st.selectbox(
         "Choose query",
         [
            "Ride Volume Over Time",
            "Booking Status Breakdown",
            "Top 5 Vehicle Types by Ride Distance",
            "Average Customer Ratings by Vehicle Type",
            "Canceled Rides Reasons",
            "Revenue by Payment Method",
            "Top 5 Customers by Total Booking Value",
            "Ride Distance Distribution Per Day",
            "Driver Ratings Distribution",
            "Customer vs. Driver Ratings"
         ]
    )  


    df["Date"] = pd.to_datetime(df["Date"])

    if query=="Ride Volume Over Time":
        result=(df.groupby(df["Date"].dt.date).size().reset_index(name="Total_Rides"))
        st.dataframe(result)
    
    

        fig=px.line(
        result,
        x="Date",
        y="Total_Rides",
        title="Ride Volume Over Time"
        )
        st.plotly_chart(fig)


    if query=="Booking Status Breakdown":
        result=df.groupby("Booking_Status").size().reset_index(name="Total_ride")
        st.dataframe(result)

    
        fig=px.bar(
        result,
        x="Booking_Status",
        y="Total_ride",
        title="Booking Status Breakdown"
        )
        st.plotly_chart(fig)

    if query=="Top 5 Vehicle Types by Ride Distance":
        result=df.groupby("Vehicle_Type")["Ride_Distance"].sum().reset_index().sort_values(by="Ride_Distance",ascending=False).head(5)
        st.dataframe(result)
    

        fig=px.bar(
        result,
        x="Vehicle_Type",
        y="Ride_Distance",
        title="Top 5 Vehicle Types by Ride Distance"
        )
        st.plotly_chart(fig)

    if query=="Average Customer Ratings by Vehicle Type":
        result=round(df.groupby("Vehicle_Type")["Customer_Rating"].mean().reset_index(),2)
        st.dataframe(result)
     
    
        fig=px.bar(
        result,
        x="Vehicle_Type",
        y="Customer_Rating",
        title="Average Customer Ratings by Vehicle Type"
        )
        st.plotly_chart(fig)

    if query=="Canceled Rides Reasons":
        result=df.groupby("Incomplete_Rides_Reason").size().reset_index(name="Total_canceletion")
        st.dataframe(result)
   

        fig=px.pie(
        result,
        names="Incomplete_Rides_Reason",
        values="Total_canceletion",
        title="Canceled Rides Reasons"
        )
        st.plotly_chart(fig)

    if query=="Revenue by Payment Method":
        result=df.groupby("Payment_Method").size().reset_index(name="Total payment")
        st.dataframe(result)
     
        fig=px.bar(
        result,
        x="Payment_Method",
        y="Total payment",
        title="Revenue by Payment Method"
        )
        st.plotly_chart(fig)

    if query=="Top 5 Customers by Total Booking Value":
        result=df.groupby("Customer_ID")["Booking_Value"].sum().sort_values(ascending=False).reset_index(name="Total Booking").head()
        st.dataframe(result)
    

        fig=px.bar(
        result,
        x="Customer_ID",
        y="Total Booking",
        title="Top 5 Customers by Total Booking Value"
        )
        st.plotly_chart(fig)

    if query=="Ride Distance Distribution Per Day":
        result=df.groupby(df["Date"].dt.date)["Ride_Distance"].sum().reset_index(name="Total distance")
        st.dataframe(result)
    
    
        fig=px.line(
        result,
        x="Date",
        y="Total distance",
        title="Ride Distance Distribution Per Day"
        )
        st.plotly_chart(fig)

    if query=="Driver Ratings Distribution":
        result=df["Driver_Ratings"].value_counts().reset_index(name="frequency")
        st.dataframe(result)
    

        fig,ax=plt.subplots()
        ax.hist(df["Driver_Ratings"], bins=10)
        ax.set_xlabel="Driver_Ratings",
        ax.set_yplot="frequency",
        ax.set_title="Driver Ratings Distribution"

        st.pyplot(fig)  


    if query=="Customer vs. Driver Ratings":
        
        result=df.groupby("Customer_Rating")["Driver_Ratings"].mean().reset_index()
        st.dataframe(result)
    

        fig=px.line(
        result,
        x="Customer_Rating",
        y="Driver_Ratings",
        title="Customer vs. Driver Ratings"
        )

        st.plotly_chart(fig)

    