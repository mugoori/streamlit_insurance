import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import platform
import altair as alt
import plotly.express as px

def run_eda_app() :
    st.subheader('사용된 데이터 프레임')
    df = pd.read_csv('i_data/insurance.csv')
    df = df.rename(columns={'sex':'gender'})
    df = df.replace('female',0)
    df = df.replace('male',1)
    df = df.replace('yes',1)
    df = df.replace('no',0)
    st.dataframe(df.head(3))

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

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


    st.subheader('상관 관계')
    selected_list = st.multiselect('상관 분석을 하고싶은 컬럼을 선택하세요',column)

    if len(selected_list) >= 2 :

        df_corr = df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr,annot=True, fmt='.2f',cmap='coolwarm',vmin=-1,vmax=1,linewidths=0.5)
        st.pyplot(fig2)   
