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
    
    auth_exp = st.expander('Auth', expanded=True)
    sb = st.sidebar()
    with sb:
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
                sb.write(f'Welcome *{st.session_state["name"]}*')
                sb.title('Some content')
            elif st.session_state["authentication_status"] is False:
                sb.error('Username/password is incorrect')
            elif st.session_state["authentication_status"] is None:
                sb.warning('Please enter your username and password')

if __name__ == "__main__":
    main()
