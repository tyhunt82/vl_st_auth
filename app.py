import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from components.login import get_login, get_config_read, get_auth

# References -----------------------------------------
# Streamlit-autherticator -> https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io

# Session vars
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False

if "auth_config_read" not in st.session_state:
    st.session_state["auth_config_read"] = get_config_read()

if "authenticator" not in st.session_state:
    st.session_state["authenticator"] = get_auth(st.session_state["auth_config_read"])

#  Main ----------------------------------------------
def main():
    if st.session_state["authentication_status"] == False:
        get_login()

    elif st.session_state["authentication_status"]:
        st.title("Welcome to the SkulptGPT AI App")
       


if __name__ == "__main__":
    main()
