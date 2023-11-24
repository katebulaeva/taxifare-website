import streamlit as st

'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')



# st.write('Let\'s ask for:')
# date_time = st.date_input('Date', help='Select the date and time')
# pickup_longitude = st.number_input('Pickup Longitude', help='Enter the pickup longitude')
# pickup_latitude = st.number_input('Pickup Latitude', help='Enter the pickup latitude')
# dropoff_longitude = st.number_input('Dropoff Longitude', help='Enter the dropoff longitude')
# dropoff_latitude = st.number_input('Dropoff Latitude', help='Enter the dropoff latitude')
# passenger_count = st.number_input('Passenger Count', help='Enter the number of passengers')

col1, col2 = st.columns(2)

with col1:
    date_time = st.date_input('Date', key='date_input', help='Select the date and time')
    passenger_count = st.number_input('Passenger Count', min_value=1, max_value=10, step=1, value=1, format="%d", help='Enter the number of passengers')


with col2:
    pickup_longitude = st.number_input('Pickup Longitude', help='Enter the pickup longitude')
    pickup_latitude = st.number_input('Pickup Latitude', help='Enter the pickup latitude')
    dropoff_longitude = st.number_input('Dropoff Longitude', help='Enter the dropoff longitude')
    dropoff_latitude = st.number_input('Dropoff Latitude', help='Enter the dropoff latitude')
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
