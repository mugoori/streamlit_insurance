import streamlit as st
from app_home import run_home_app

def main() :
    st.title('insurance predict app')

    menu = ['Home']
    choice = st.sidebar.selectbox('메뉴',menu)
    if choice == 'Home' :
        run_home_app()

if __name__ == '__main__' :
    main()