# import streamlit as st
#
# st.title("welcome to your website")
# st.header("welcome to your website")
# st.subheader("welcome to your website")
# st.code("""for i in range (1,5,1):
#                print("hello print")""")


# dataset = pd.read_csv("continent.csv")
# st.dataframe(dataset)
import streamlit as st
import pandas as pd
from streamlit import button

name = st.text_input("Enter your name")
f_name = st.text_input("Enter your f_name")
adr = st.text_input("Enter your adress")
classdata = st.selectbox("Select your class :",(1,2,3,4,5))
button = st.button("Done")
if button:
    st.markdown(f"""
        Name: {name}    
        Father Name: {f_name}
        Address: {adr}
        Class: {classdata}  """)