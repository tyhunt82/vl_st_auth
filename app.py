import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from components.login import get_login, get_logout, get_auth

# References -----------------------------------------
# Streamlit-autherticator -> https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io

# Session vars
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False

# if "authenticator" not in st.session_state:
#     st.session_state["authenticator"] = get_auth()

#  Main ----------------------------------------------
def main():
    if st.session_state["authentication_status"] == False:
        get_login()

    elif st.session_state["authentication_status"]:
        st.title("Welcome to the SkulptGPT AI App")
        with st.sidebar:
            get_logout()
       


if __name__ == "__main__":
    main()
