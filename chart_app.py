import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart_app() :

    
    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')

    st.title('Bar Chart')

    st.subheader(' 지역별 리뷰 수 ')
    fig1 = plt.figure()
    df['province'].hist()
    st.pyplot(fig1)
    

    st.subheader(' 점수대별 리뷰 수 ')
    fig2 = plt.figure()
    df['points'].hist()
    st.pyplot(fig2)

    print(df['province'].nunique)