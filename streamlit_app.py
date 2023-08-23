import streamlit
import pandas
streamlit.title('welcome to my first app 🥣')
streamlit.header('Hello 🥑')
streamlit.text('welcome 🐔')
streamlit.text('to My ')
streamlit.text('page! 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruite_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruite_list)
