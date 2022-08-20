import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# another header menu
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import file from S3 bucket - fruit_macros.txt
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# want to see names in picklist
my_fruit_list = my_fruit_list.set_index('Fruit')

# put some multiselect for user to pick the fruits from the list, also we prepopulate as example for user
fruits_selected = streamlit.multiselect('Picked some fruit:', list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# show dataframe in streamlit app
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

import requests

BASE_URL = "https://fruityvice.com/api/fruit/"
# Get input from user for fruit
fruit_choice = streamlit.text_input("What fruit would you like the information about?",'kiwi')
streamlit.write('Your choice is ', fruit_choice)

fruityvice_response = requests.get(BASE_URL + fruit_choice)
# streamlit.text(fruityvice_response.json())  # shows only json data

# normalize json data using python
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output json normalized data as table
streamlit.dataframe(fruityvice_normalized)

# snowflake python connector
import snowflake.connector

# check some data from tables
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
