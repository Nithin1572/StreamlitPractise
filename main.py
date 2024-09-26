import streamlit as st  # type: ignore
import mysql.connector # type: ignore

st.write("## Enter you Details :")

x = st.text_input("Enter data to insert or Enter table name to view")

col1, col2, col3 = st.columns(3)

with col1:
    insertButton = st.button("Insert")
with col2:
    showAllRecordsButton = st.button("Data")
with col3:
    showAllTables = st.button("Tables")

conn = mysql.connector.connect(
        host = st.secrets["mysql"]["hostname"],
        user = st.secrets["mysql"]["username"],
        password = st.secrets["mysql"]["password"],
        database = st.secrets["mysql"]["database"]
    )
cursor = conn.cursor()

showAllRecordsQuery = "select * from " + x + ";"
showTables = "show tables;"
insertQuery = "insert into users values(" + '"' + x + '"' + ");"
    
if insertButton and x != "":
    cursor.execute(insertQuery)
    st.write(f"Data Inserted!")
elif showAllRecordsButton and x != "":
    cursor.execute(showTables)
    result = cursor.fetchall()
    isPresent = False
    for tableName in result:
        if tableName[0] == x:
            isPresent = True
    if isPresent:
        cursor.execute(showAllRecordsQuery)
        result = cursor.fetchall()
        if result != "":
            for x in result:
                st.write(x[0])
    else:
        st.write("Enter a valid table name")
elif showAllTables:
    cursor.execute(showTables)
    result = cursor.fetchall()
    for tableName in result:
        st.write(tableName[0])

conn.commit() 
cursor.close()
conn.close()