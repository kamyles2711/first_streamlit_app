import streamlit as sl
import pandas as pd
import requests
import snowflake.connector
import urllib.error as URLError

sl.title('My Parents New Healthy Diner')

sl.header('Breakfast Menu')

sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = sl.multiselect("Pick some fruits:", list(fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

 
# Display the table on the page.
sl.dataframe(fruits_to_show)

#Function to display FruityVice API Response
sl.header('Fruityvice Fruit Advice!')
def get_fruityvice_data(this_fruit_):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
 
#New section to display fruityvice API response
try:
 fruit_choice = sl.text_input('What fruit would you like information about?')
 if not fruit_choice:
  sl.error('Please select a fruit to get information.')
 else:
  back_from_function = get_fruityvice_data(fruit_choice)
  sl.dataframe(back_from_function)
except URLError as e:
 sl.error()

sl.stop()

#Snowflake Connection
my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
sl.header("The fruit load list contains:")
sl.dataframe(my_data_rows)

#Allow user to add fruit to the list
add_fruit = sl.text_input('What fruit would you like to add?','jackfuit')
sl.write('Thanks for adding ', add_fruit)

