import streamlit as st


def get_camera_output():
    st.markdown('## Camera')
    img_file_buffer = st.camera_input(label="Empty", label_visibility="collapsed")
    return img_file_buffer