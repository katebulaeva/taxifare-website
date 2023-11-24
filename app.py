import streamlit as st
import requests
from datetime import datetime


# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')


col1, col2 = st.columns(2)

with col1:
    #date_time = st.date_input('Date', key='date_input', help='Select the date and time')
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    passenger_count = st.number_input('Passenger Count', min_value=1, max_value=10, step=1, value=1, format="%d", help='Enter the number of passengers')


with col2:
    pickup_longitude = st.number_input('Pickup Longitude', help='Enter the pickup longitude')
    pickup_latitude = st.number_input('Pickup Latitude', help='Enter the pickup latitude')
    dropoff_longitude = st.number_input('Dropoff Longitude', help='Enter the dropoff longitude')
    dropoff_latitude = st.number_input('Dropoff Latitude', help='Enter the dropoff latitude')

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''


url0 = 'https://taxifare.lewagon.ai/predict'

if url0 == 'https://taxifare.lewagon.ai/predict':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


    params = {
    'pickup_datetime': str(f"{date} {time}"),
    'passenger_count': int(passenger_count),
    'pickup_longitude': float(pickup_longitude),
    'pickup_latitude': float(pickup_latitude),
    'dropoff_longitude': float(dropoff_longitude),
    'dropoff_latitude': float(dropoff_latitude)
    }




if st.button('Predict'):
    query = '&'.join([f"{key}={value}" for key, value in params.items()])
    url = f"{url0}?{query}"
    #st.write('Кнопка была нажата!')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fare = round(response.json()['fare'], 2)
            st.write(f"Predicted fare: ${fare}")
        else:
            #st.write(url)
            st.write("Failed to fetch prediction. Please check the API endpoint and parameters.")
    except requests.RequestException as e:
        st.write(f"Error: {e}")
#st.button()
