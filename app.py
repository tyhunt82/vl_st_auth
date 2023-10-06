import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# References -----------------------------------------
# Streamlit-autherticator -> https://github.com/mkhorasani/Streamlit-Authenticator?ref=blog.streamlit.io

def main():
    st.title("Welcome to the SkulptGPT AI App")

    # Read in yaml
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    
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
            <a href="https://your-site.com/forgot-username" target="_blank">Forgot Username</a> |
            <a href="https://your-site.com/forgot-password" target="_blank">Forgot Password</a> |
            <a href="https://your-site.com/register" target="_blank">Register New</a>
        </div>
        """
    st.markdown(links, unsafe_allow_html=True)


    if st.session_state["authentication_status"]:
        with st.sidebar:
            authenticator.logout('Logout', 'main', key='unique_key')
            st.write(f'Welcome *{st.session_state["name"]}*')

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')

    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    

if __name__ == "__main__":
    main()
