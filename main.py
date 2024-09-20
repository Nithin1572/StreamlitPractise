import streamlit as st  # type: ignore

st.write("## Enter you Details :")

x = st.text_input("Enter your name")

if x != "":
    st.write(f"hello, {x}!")
