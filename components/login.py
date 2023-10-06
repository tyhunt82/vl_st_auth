import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def get_login():
    with open('config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)

    login_cont = st.container()

    with login_cont:
        authenticator = stauth.Authenticate(
                config['credentials'],
                config['cookie']['name'],
                config['cookie']['key'],
                config['cookie']['expiry_days'],
                config['preauthorized']
            )

        authenticator.login('Login', 'main')
    links = """
        <div style="text-align: center;">
            <a href="#" target="_blank"> Forgot Username</a>  | 
            <a href="#" target="_blank"> Forgot Password</a>  | 
            <a href="#" target="_blank"> Register New</a>
        </div>
        """
    st.markdown(links, unsafe_allow_html=True)