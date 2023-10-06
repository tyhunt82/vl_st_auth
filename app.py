import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from components.login import get_login

# References -----------------------------------------
# Streamlit-autherticator -> https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io

# set default case
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False


def main():
    st.title("Welcome to the SkulptGPT AI App")
    st.sidebar()

    if st.session_state["authentication_status"]==False:
        get_login()

    elif st.session_state["authentication_status"] == False:
        str.write("Logged in")


if __name__ == "__main__":
    main()
