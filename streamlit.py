import streamlit as st
st.title("NIVEDITHA'S 1ST APP")
n=st.write("HELLO")
st.text_input("enter your name")
st.number_input("enter your age")
if st.button("SUBMIT"):
  st.write("welcome")

