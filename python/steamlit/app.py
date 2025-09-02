#streamlit is a open source framework for aiml,ds prject,it help in create web application
import streamlit as st
import pandas as pd
import numpy as np
st.title("hello")
#simple text
st.write("simple text")
df=pd.DataFrame({
    "first col":[1,3,5,7],
    "second col":[2,4,6,8]
})
st.write("data frame")
st.write(df)

#input
name=st.text_input("enter name")
age=st.slider("enter age",0,100,25)
if name:
    st.write(f"hello {name}")

#select box
options=['a','b','c','d']
op=st.selectbox("enter choice",options)
st.write("selected :"+op)

#upload
up=st.file_uploader("choose file csv",type="csv")

df=pd.read_csv(up)
st.write(df)