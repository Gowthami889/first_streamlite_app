import streamlit
import pandas
streamlit.title('welcome to my first app 🥣')
streamlit.header('Hello 🥑')
streamlit.text('welcome 🐔')
streamlit.text('to My ')
streamlit.text('page! 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruite_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruite_list =my_fruite_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruite_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
