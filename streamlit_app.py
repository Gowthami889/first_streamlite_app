import streamlit
import pandas as pd

streamlit.title('welcome to my first app 🥣')

streamlit.header('Hello 🥑')
streamlit.text('welcome 🐔')
streamlit.text('to My ')
streamlit.text('page! 🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruite_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruite_list)
