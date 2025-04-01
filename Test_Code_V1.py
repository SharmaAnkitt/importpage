import streamlit as st

st.header("View Any Video, Just paste the URL")
st.title("First App")

a = str(st.text_input("Input URL:"))

try:
    st.video(a)
except Exception as e:
    st.write("Enter URL")
