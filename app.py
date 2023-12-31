import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from components.login import get_login, get_logout, get_auth

# References -----------------------------------------
# Streamlit-autherticator -> https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io
# https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io


# Session vars
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False


#  Main ----------------------------------------------
def main():
    if st.session_state["authentication_status"] is False:
        st.title("Welcome to the SkulptGPT AI App")
        get_login()

    elif st.session_state["authentication_status"] is True:
        st.title("Welcome to the SkulptGPT AI App")
        st.write("Hello")
       


if __name__ == "__main__":
    main()
