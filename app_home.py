import streamlit as st
import numpy as np
import joblib


def run_home_app() :
    st.balloons()
    # ------- 풍선 날리기


    st.video('https://www.youtube.com/watch?v=47cAxRX3aDg&t=0s')
    # ------- 동영상 보여주기


    st.subheader('환영합니다.')
    st.subheader('좌측 사이드바에 데이터를 넣으면 보험료를 예측해줍니다.')
    # ------- 홈 화면 문자 표시


    age = st.sidebar.number_input('나이 입력',18,100)
    gender = st.sidebar.radio('성별 선택',['여자','남자'])
    if gender == '남자' :
        gender = 1
    else :
        gender = 0
    smoker = st.sidebar.radio('흡연 유무',['흡연','비흡연'])
    if smoker == '흡연' :
        smoker = 1
    else :
        smoker = 0
    bmi = st.sidebar.number_input('체질량지수 입력',15.0,50.0)
    children = st.sidebar.number_input('자녀 수 입력',0,10)
    # -------- 리그레서에 들어갈 예상 데이터인 뉴 데이터 입력받기


    new_data = np.array([age,gender,bmi,children,smoker])
    new_data = new_data.reshape(1,5)
    # --------- 입력 받은 뉴 데이터 변수 저장 및 리쉐이브


    regressor = joblib.load('regressor.pkl')
    # --------- 리그레서 불러오기


    y_pred = regressor.predict(new_data)
    y_pred = round(y_pred[0])
    # ---------  결과값 예측해서 저장하기
    
   
    st.sidebar.text('당신의 예상 보험료는 {} 달러 입니다.'.format(y_pred))
    # ---------  결과값 보여주기