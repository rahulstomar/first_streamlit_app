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

# show dataframe in streamlit app
streamlit.dataframe(my_fruit_list)

# put some multiselect for user to pick the fruits from the list
streamlit.multiselect('Picked some fruit:', list(my_fruit_list.index))
