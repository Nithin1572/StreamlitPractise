import streamlit as st  # type: ignore
import mysql.connector # type: ignore

st.write("## Enter you Details :")

x = st.text_input("Enter your name")
isClicked = st.button("Enter")

#host user password database

if isClicked and x != "":
    conn = mysql.connector.connect(
        host = st.secrets["mysql"]["hostname"],
        user = st.secrets["mysql"]["username"],
        password = st.secrets["mysql"]["password"],
        database = st.secrets["mysql"]["database"]
    )

    cursor = conn.cursor()
    q1 = "insert into users values(" + '"' + x + '"' + ");"

    cursor.execute(q1)

    conn.commit() 
    cursor.close()
    conn.close()

    st.write(f"Data Inserted!")