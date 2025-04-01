import streamlit as st


a = str(st.text_input("Input URL:"))

try:
    st.video(a)
except Exception as e:
    st.write("Enter URL")