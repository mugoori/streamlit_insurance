import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import platform
import altair as alt
import plotly.express as px

def run_home_app() :

    st.subheader('환영합니다.')
    st.subheader('좌측 사이드바에 데이터를 넣으면 보험료를 예측해줍니다.')
    # ------- 홈 화면 문자 표시


    st.video('https://www.youtube.com/watch?v=47cAxRX3aDg&t=0s')
    # ------- 동영상 보여주기


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
    bmi = st.sidebar.number_input('체질량 지수',15.0,50.0)
    children = st.sidebar.number_input('자녀 수',0,10)
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



    df = pd.read_csv('i_data/insurance.csv')
    df = df.rename(columns={'sex':'gender'})
    df = df.replace('female',0)
    df = df.replace('male',1)
    df = df.replace('yes',1)
    df = df.replace('no',0)
    # ----------------------------- 데이터 가공


    show_df = st.checkbox('데이터 프레임')
    if show_df :
        st.dataframe(df.head(3))
    show_df2 = st.checkbox('기초 통계')
    if show_df2 :
        st.dataframe(df.describe())
    # ----------------------------  데이터 프레임 / 기초 통계 보여주기


    st.subheader('컬럼 별 히스토그램')
    column = df.columns[0:]
    choice2 = st.selectbox('컬럼을 선택하세요',column)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 2, 30, value=2, step=1)

    fig = plt.figure()
    plt.hist(data=df , x= choice2, rwidth=0.8, bins=my_bins)
    plt.title( choice2 +' histogram')
    plt.xlabel(choice2)
    plt.ylabel('Count')
    st.pyplot(fig)
    # --------------------------- 컬럼 별 히스토그램 보여주기


    st.subheader('상관 관계')
    selected_list = st.multiselect('상관 분석을 하고싶은 컬럼을 선택하세요',column)

    if len(selected_list) >= 2 :

        df_corr = df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr,annot=True, fmt='.2f',cmap='coolwarm',vmin=-1,vmax=1,linewidths=0.5)
        st.pyplot(fig2)   
    # -------------------------- 컬럼 별 상관관계 보여주기
