import streamlit as st

session_state = st.session_state
session_state["page"] = "home"

page = st.sidebar.radio("navigate",["home","about"])

if page == "home":
    st.write("home page")
elif page == "about":
    st.title("about page")
