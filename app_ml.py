import streamlit as st
import numpy as np
import joblib

def run_ml_app() :
    
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

    new_data = np.array([age,gender,bmi,children,smoker])
    new_data = new_data.reshape(1,5)

    regressor = joblib.load('regressor.pkl')

    y_pred = regressor.predict(new_data)
    y_pred = round(y_pred[0])

    st.image('https://cdn.jjalbot.com/2019/11/WodIAGgOBT/-neQ5msQk.png')
    st.subheader('당신의 예상 보험료는 {} 달러 입니다.'.format(y_pred))

