import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from PIL import Image
img = Image.open('i_data/img1.jpg')
st.set_page_config(page_title='insurance predict app',
page_icon=img,layout ='wide' , initial_sidebar_state = 'collapsed')

def main() :

    st.title('insurance predict app')

    menu = ['Home','EDA']
    choice = st.sidebar.selectbox('메뉴',menu)
    if choice == 'Home' :
        run_home_app()
    if choice == 'EDA' :
        run_eda_app()

if __name__ == '__main__' :
    main()

