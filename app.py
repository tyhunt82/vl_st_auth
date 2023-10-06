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
    
    hashed_passwords = stauth.Hasher(['abc123', 'abc123']).generate()
    st.write(hashed_passwords)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    authenticator.login('Login', 'main')

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main', key='unique_key')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()
