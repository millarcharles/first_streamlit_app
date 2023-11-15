import streamlit
import pandas as pd

streamlit.header('Breakfast Menu')
  
streamlit.text('Omega 3 and Blueberry Oatmeal 🥣')
streamlit.text('Kale, Spinach and Rocket Smoothie 🥗 ')
streamlit.text('Hard Boiled, Free-range Eggs 🐔')
streamlit.text('Avocado Toast 🥑🍞')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


