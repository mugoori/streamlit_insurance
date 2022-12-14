import streamlit as st

def run_home_app() :
    st.text('환영합니다.')
    st.text('이 앱은 고객 데이터를 넣으면 보험료를 예측하는 앱 입니다.')

    img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEHasrsrR0LlovHF2K5_q2dWiDIz7S9TPD7g&usqp=CAU'
    st.image(img_url)