import streamlit as st
from stream_option_menu import option_menu
st.title("my live application")
with st.sidebar:
data = option_menu(
  menu_title = "my apps",
  options=["home","about","service"],
)
