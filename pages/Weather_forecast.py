import streamlit as st
import plotly.express as px
from Weather_backend import get_data

#st.set_page_config(layout="wide")
st.title('Weather Forecast')

place = st.text_input('Place')
#this API only gives 5 days of data
days = st.slider("Forecast Days", min_value = 1,max_value = 5, help = "Select the number of forecasted days")

choice = st.selectbox("Select data to view",['Temperature in C', 'Forecast'])

if days == 1:
    st.subheader(f"{choice} for the next {days} day in {place}")
else:
    st.subheader(f"{choice} for the next {days} days in {place}")

#check if place is provided
if place:
    #if place is provided try to get data
    try:
        #Get the temperature/forecastdata, cannot use forecast_days cos not yet defined
        filtered_content = get_data(place,days)

        #filter further by choice of temperature or forecast
        if choice == "Temperature in C":
        #create a temperature plot
            temperatures=[dict["main"]["temp"] for dict in filtered_content]
            #dt_txt for that particular date time format
            dates = [dict["dt_txt"] for dict in filtered_content]
            figure = px.line(x=dates,y= temperatures,labels = {"x":"Date", "y":"Temperature in C"})
            st.plotly_chart(figure)

        if choice == "Forecast":
            images = {"Clear":"skyimages/clear.png","Clouds":"skyimages/cloud.png","Rain":"skyimages/rain.png","Snow":"skyimages/snow.png"}
            dates = [dict["dt_txt"] for dict in filtered_content]
            skyforecast = [dict["weather"][0]["main"] for dict in filtered_content]

            for i,forecast in enumerate(skyforecast):
                if forecast == "Clouds":
                    st.image("skyimages/cloud.png", width = 115)
                    # put [0:-3 cos dont want the seconds of the time]
                    st.write(f" {forecast} | {dates[i][0:-3]}" )

                elif forecast == "Clear":
                    st.image("skyimages/clear.png", width=115)
                    st.write(f" {forecast} | {dates[i][0:-3]}")
                elif forecast == "Rain":
                    st.image("skyimages/rain.png", width=115)
                    st.write(f" {forecast} | {dates[i][0:-3]}")

                elif forecast == "Snow":
                    st.image("skyimages/snow.png", width=115)
                    st.write(f" {forecast} | {dates[i][0:-3]}")
                else:
                    st.write("Weather data not available")



    #if invalid place provided, show error message
    except KeyError:
        st.write('Please type a valid location')