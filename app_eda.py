import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app() :
    st.sidebar.image('https://img.hankyung.com/photo/202002/AA.21765513.1.jpg')
    # ----------------------------- 사이드바 이미지
    
    df = pd.read_csv('i_data/insurance.csv')
    df = df.rename(columns={'sex':'gender'})
    df = df.replace('female',0)
    df = df.replace('male',1)
    df = df.replace('yes',1)
    df = df.replace('no',0)
    df2 = pd.read_csv('i_data/df2.csv') # df2 는 컬럼의 순서를 바꿨다
    # ----------------------------- 데이터 가공

    st.subheader('각 컬럼별 의미')
    st.text('age : 나이')
    st.text('gender : 성별 여 0 남 1')
    st.text('bmi : 체질량 지수')
    st.text('children : 자녀의 수')
    st.text('smoker : 비흡연 0 흡연 1')
    st.text('charges : 보험료')    
    # ----------------------------- 각 컬럼별 설명

    st.subheader('사용된 데이터 프레임 및 기초 통계')
    show_df = st.checkbox('사용된 데이터 프레임')
    if show_df :
        st.dataframe(df.head(3))
    show_df2 = st.checkbox('기초 통계')
    if show_df2 :
        st.dataframe(df.describe())
    # ----------------------------  데이터 프레임 / 기초 통계 보여주기

    st.subheader('나이,체질량,보험료의 최대 최소값')
    column_list = df2.columns[1:4]
    selected_column = st.radio('컬럼을 선택하세요',column_list)   
    df_max = df2.loc[df[selected_column] == df2[selected_column].max(),]
    df_min = df2.loc[df[selected_column] == df2[selected_column].min(),]

    st.dataframe(df_max)
    st.dataframe(df_min)
    # --------------------------- 데이터의 최대 최소값


    st.subheader('각 컬럼 별 히스토그램')
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
    selected_list = st.multiselect('보험료의 증감 유무를 알고 싶은 컬럼을 선택하세요',column,default='charges')

    if len(selected_list) >= 2 :

        df_corr = df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr,annot=True, fmt='.2f',cmap='coolwarm',vmin=-1,vmax=1,linewidths=0.5)
        st.pyplot(fig2)   
    # -------------------------- 컬럼 별 상관관계 보여주기