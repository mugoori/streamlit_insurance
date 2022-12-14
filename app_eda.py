import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda_app() :
    st.subheader('사용된 데이터 프레임')
    df = pd.read_csv('i_data/insurance.csv')
    df = df.rename(columns={'sex':'성별'})
    df = df.rename(columns={'age':'나이'})
    df = df.rename(columns={'bmi':'체질량지수'})
    df = df.rename(columns={'children':'자녀'})
    df = df.rename(columns={'smoker':'흡연유무'})
    df = df.rename(columns={'region':'지역'})
    df = df.rename(columns={'charges':'보험료'})
    df = df.replace('female',0)
    df = df.replace('male',1)
    df = df.replace('yes',1)
    df = df.replace('no',0)
    st.dataframe(df.head(3))

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대 / 최소 데이터 확인하기')
    



