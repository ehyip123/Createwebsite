import streamlit as st
import plotly.express as px
from Weather_backend import get_data

st.title('Weather Forecast')

place = st.text_input('Place')
#this API only gives 5 days of data
days = st.slider("Forecast Days", min_value = 1,max_value = 5, help = "Select the number of forecasted days")

choice = st.selectbox("Select data to view",['Temperature in C', 'Sky'])

if days == 1:
    st.subheader(f"{choice} for the next {days} day in {place}")
else:
    st.subheader(f"{choice} for the next {days} days in {place}")

#check if place is provided
if place:
    #Get the temperature/sky data, cannot use forecast_days cos not yet defined
    filtered_content = get_data(place,days)

    #filter further by choice of temperature or sky condition
    if choice == "Temperature in C":
    #create a temperature plot
        temperatures=[dict["main"]["temp"] for dict in filtered_content]
        #dt_txt for that particular date time format
        dates = [dict["dt_txt"] for dict in filtered_content]
        figure = px.line(x=dates,y= temperatures,labels = {"x":"Date", "y":"Temperature in C"})
        st.plotly_chart(figure)

    if choice == "Sky":
        filtered_content = [dict["weather"][0]["main"] for dict in filtered_content]
        st.image()