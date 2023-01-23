# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 07:13:37 2023

@author: stevi
"""

import requests
import streamlit as st

st.title('Weather App')

st.markdown("""
This app retrieves the weather from any city in the worls the user choses!
* **Python libraries:** requests, streamlit
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

    part = 'minutely'

    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&exclude={part}&appid="
    final_url = weather_url + API_Key
    weather_data = requests.get(final_url).json()
    return weather_data

#print(weather_data)

if st.button('Show me the weather!'):
    st.subheader('The weather in ')
    st.usbheader(city)
    st.subheader(' is:')
    get_weather(city)
else:
    st.write('Click the button to display the weather in your city of choice')
