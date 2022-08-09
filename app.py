import streamlit as st
import joblib

#load the joblib model
model_nb=joblib.load("spam-ham")
st.title("spam ham classifierq  ")
ip=st.text_input("enter the text:")
op=model_nb.predict([ip])
if st.button("predict"):
  st.title(op[0])
