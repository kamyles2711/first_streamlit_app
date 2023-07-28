import streamlit as sl
import pandas as pd

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
sl.multiselect("Pick some fruits:", list(fruit_list.index), ['Avocado', 'Starwberries'])

# Display the table on the page.
sl.dataframe(fruit_list)

