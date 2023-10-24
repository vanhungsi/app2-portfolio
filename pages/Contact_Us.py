import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    massage = st.text_area("Your massage")
    button = st.form_submit_button()