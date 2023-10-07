import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import uuid

def get_auth():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    return stauth.Authenticate(
                config['credentials'],
                config['cookie']['name'],
                config['cookie']['key'],
                config['cookie']['expiry_days'],
                config['preauthorized'],
                key=uuid.uuid1
            )

def get_login():

    login_cont = st.container()

    with login_cont:
        authenticator = get_auth(get_config_read())
        authenticator.login('Login', 'main')
        links = """
        <div style="text-align: center;">
            <a href="#" target="_blank"> Forgot Username</a>  | 
            <a href="#" target="_blank"> Forgot Password</a>  | 
            <a href="#" target="_blank"> Register New</a>
        </div>
        """
        st.markdown(links, unsafe_allow_html=True)
    return login_cont

def get_logout():
    logout_cont = st.container()

    with logout_cont:
        authenticator = get_auth()
        authenticator.logout('Logout', 'sidebar', key=uuid.uuid1)
    return logout_cont