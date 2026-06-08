import streamlit as st
from streamlit_option_menu import option_menu

st.title("My Live Application")

with st.sidebar:
    data = option_menu(
        menu_title="My Apps",
        options=["Home", "About", "Service"],
    )

st.write("Selected:", data)
