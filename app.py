import streamlit as st
from components.side_bar import show_side_bar
from components.camera_input import get_camera_output
from components.header import show_header
from components.results import get_results, show_results

def main():
    st.set_page_config(
        page_title="Final Project", 
        page_icon="🧊", 
        initial_sidebar_state="collapsed", 
        layout='wide',
        menu_items=None
    )
    selected = show_side_bar()
    show_header()
    if selected == "Camera":
        col1, col2 = st.columns([4, 1], gap='medium')
        with col1:
            img_file_buffer = get_camera_output()
        with col2:
            results = get_results(img_file_buffer)
            show_results(results)
    elif selected == "Information": 
        st.write("Information")

if __name__ == "__main__":
    main()