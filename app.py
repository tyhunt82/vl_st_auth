import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# References -----------------------------------------
# Streamlit-autherticator -> https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io

def main():
    st.title("Welcome to the SkulptGPT AI App")

    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    
   

    with st.sidebar:
        auth_exp = st.expander('Auth', expanded=True)
        with auth_exp:
            authenticator = stauth.Authenticate(
                config['credentials'],
                config['cookie']['name'],
                config['cookie']['key'],
                config['cookie']['expiry_days'],
                config['preauthorized']
            )

        authenticator.login('Login', 'sidebar')

        if st.session_state["authentication_status"]:
            authenticator.logout('Logout', 'sidebar', key='unique_key')
            st.write(f'Welcome *{st.session_state["name"]}*')
        elif st.session_state["authentication_status"] is False:
            st.error('Username/password is incorrect')
        elif st.session_state["authentication_status"] is None:
            st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()
