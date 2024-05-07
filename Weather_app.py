# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 07:13:37 2023

@author: stevi
"""

import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.title('Weather App')

st.markdown("""
This app retrieves the weather from any city in the world the user choses!
* **Python libraries:** requests, streamlit, pandas, pyplot
* **Data source:** OpenWeather API.
""")

city = st.text_input('Input a City', 'Park City')
st.write('Your current selected city is', city)

def get_weather(location):
    

    API_Key = "3014d47cf62ff4109d203a2ec132799a"

#location = input("Enter Your Desired Location: ")
#location = city

    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&appid="
    final_geo_url = geo_url + API_Key
    geo_data = requests.get(final_geo_url).json()

    keys = [i for i in range(len(geo_data))]
    my_dict = dict(zip(keys, geo_data))

    geo_dict = my_dict[0]

    lat = geo_dict['lat']
    long = geo_dict['lon']

#print(lat,long)
    
    part = 'current, minutely, hourly, alerts'

    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&exclude={part}&units=imperial&appid="
    final_url = weather_url + API_Key
    weather_data = requests.get(final_url).json()
    
    # Create empty lists to store the data
    dates = []
    temperatures = []

    # Iterate through the list of forecasts and print the temperature for each day
    for forecast in weather_data["daily"]:
        dates.append(forecast["dt"])
        temperatures.append(forecast["temp"]["day"])
        
    df = pd.DataFrame({"date": dates, "temperature": temperatures})
    
    # Convert "date" column to datetime object.
    #df["date"] = pd.to_datetime(df["date"])
    #df["date"] = df["date"].dt.strftime("%a %d, %b")
    df['datetime'] = df['date'].apply(datetime.fromtimestamp)

    # Create a figure object
    fig = plt.figure()

    plt.plot(df["datetime"], df["temperature"])
    plt.xlabel("Date")
    plt.ylabel("Temperature (F)")
    
    # Rotate x-axis marker labels
    plt.xticks(rotation=45)

    #return st.caption(weather_data)
    #return st.dataframe(df)
    return st.pyplot(fig)

#print(weather_data)

if st.button('Show me the weather!'):
    st.subheader('The weather in ')
    st.subheader(city)
    st.subheader(' is:')
    get_weather(city)
else:
    st.write('Click the button to display the weather in your city of choice')
