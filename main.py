import streamlit as st  # type: ignore
import mysql.connector # type: ignore

st.write("## Enter you Details :")

x = st.text_input("Enter your name")

col1, col2 = st.columns(2)

with col1:
    insertButton = st.button("Enter Name")
with col2:
    showAllButton = st.button("Show all Records")

conn = mysql.connector.connect(
        host = st.secrets["mysql"]["hostname"],
        user = st.secrets["mysql"]["username"],
        password = st.secrets["mysql"]["password"],
        database = st.secrets["mysql"]["database"]
    )
cursor = conn.cursor()

showAllQuery = "select * from users;"
insertQuery = "insert into users values(" + '"' + x + '"' + ")"
    
if insertButton and x != "":
    cursor.execute(insertQuery)
    st.write(f"Data Inserted!")
elif showAllButton:
    cursor.execute(showAllQuery)
    result = cursor.fetchall()
    for x in result:
        st.write(x[0])

conn.commit() 
cursor.close()
conn.close()