import streamlit as st
from streamlit_option_menu import option_menu


def show_side_bar():
    with st.sidebar:
        selected = option_menu("Main Menu", ['Information', 'Camera'],
            icons=['info-square', 'webcam'], menu_icon="cast", default_index=0)
    return selected