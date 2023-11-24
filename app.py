import streamlit as st
import requests
import pandas as pd
import numpy as np
import time

img = 'https://art-vek.com/files/products/4534.1000x.png?eb6dc28cfc55c0d1027fccca644006c4'


st.sidebar.title("About")
st.sidebar.info(
    """
    This app is helping you to predict Taxi Fare in NY.
    """
)
st.sidebar.info("Feel free to collaborate and comment on the work. The github link can be found "
                "[here](https://github.com/yuliianikolaenko/COVID_dashboard_proglib).")
st.title("Predict your Taxi Fare in NY !!!")
st.sidebar.image(img, width=300)

# https://nemcd.com/wp-content/uploads/2019/11/new-york-maps.jpg'


page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://nemcd.com/wp-content/uploads/2019/11/new-york-maps.jpg");
  background-size: cover;
}
</style>
"""

#st.markdown(page_element, unsafe_allow_html=True)

# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

dash1= st.container()
with dash1:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        #date_time = st.date_input('Date', key='date_input', help='Select the date and time')
        date = st.date_input("Select Date")
        time_ = st.time_input("Select Time")
    with col2:
        passenger_count = st.number_input('Passenger Count', min_value=1, max_value=10, step=1, value=1, format="%d", help='Enter the number of passengers')


    with col3:
        pickup_longitude = st.number_input('Pickup Longitude', help='Enter the pickup longitude')
        pickup_latitude = st.number_input('Pickup Latitude', help='Enter the pickup latitude')
    with col4:
        dropoff_longitude = st.number_input('Dropoff Longitude', help='Enter the dropoff longitude')
        dropoff_latitude = st.number_input('Dropoff Latitude', help='Enter the dropoff latitude')

autos = st.multiselect("Choose auto type: ",
                         ['Sedan', 'Minivan', 'Sport'])

st.write("You selected", len(autos), 'auto')

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
    'pickup_datetime': str(f"{date} {time_}"),
    'passenger_count': int(passenger_count),
    'pickup_longitude': float(pickup_longitude),
    'pickup_latitude': float(pickup_latitude),
    'dropoff_longitude': float(dropoff_longitude),
    'dropoff_latitude': float(dropoff_latitude)
    }



style = "<style>h2 {text-align: bottom;}</style>"
st.markdown(style, unsafe_allow_html=True)

# creates the container for page title
#dash_1 = st.container()

#with dash_1:
    # st.write("")
    # st.markdown("""
    # <style>
    # .custom-button {
    # background-color: #4CAF50;
    # color: white;
    # padding: 14px 20px;
    # margin: 8px 0;
    # border: none;
    # cursor: pointer;
    # width: 100%;
    # }
    # .custom-button:hover {
    # opacity: 0.8;
    # }
    # </style>
    # <button class="custom-button">Custom Button</button>
    # """, unsafe_allow_html=True)

if st.button('Predict'):
    #st.markdown("<h2 style='text-align: center;'>PREDICTING</h2>", unsafe_allow_html=True)
    query = '&'.join([f"{key}={value}" for key, value in params.items()])
    url = f"{url0}?{query}"
    #st.write('Кнопка была нажата!')
    progress_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)
        progress_text.text(f"Progress: {i}%")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fare = round(response.json()['fare'], 2)
            st.write(f"Predicted fare: **${fare}** :sunglasses:")
            st.success("Success")
        else:
            #st.write(url)
            st.error("Error")
            st.write("Failed to fetch prediction. Please check the API endpoint and parameters.")
    except requests.RequestException as e:
        st.write(f"Error: {e}")
#st.button()



df = pd.DataFrame(np.array([[pickup_latitude,pickup_longitude],
                            [dropoff_latitude,dropoff_longitude]]),
                  columns=['lat', 'lon'])
st.map(df, use_container_width=True)















# st.title() – для установки заголовка;
# st.text() – для записи описания для конкретного графика;
# st.markdown() – для отображения текста в виде markdown;
# st.latex() – для отображения математических выражений на панели мониторинга;
# st.write() – помогает отображать все возможные детали, например, график, фрейм данных, функции, модель и т. д.;
# st.sidebar() – для отображения данных на боковой панели;
# st.dataframe() – для отображения фрейма данных;
# st.map() – для отображения карты в одной строке кода и т. д.


# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
# if st.checkbox("Show/Hide"):

#     # display the text if the checkbox returns True value
#     st.text("Showing the widget")

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
# if (status == 'Male'):
#     st.success("Male")
# else:
#     st.success("Female")



# # Selection box

# # first argument takes the titleof the selectionbox
# # second argument takes options
# hobby = st.selectbox("Hobbies: ",
#                      ['Dancing', 'Reading', 'Sports'])

# # print the selected hobby
# st.write("Your hobby is: ", hobby)




# multi select box

# first argument takes the box title
# second argument takes the options to show
# hobbies = st.multiselect("Hobbies: ",
#                          ['Dancing', 'Reading', 'Sports'])

# # write the selected options
# st.write("You selected", len(hobbies), 'hobbies')
