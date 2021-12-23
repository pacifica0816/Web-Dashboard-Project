import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart_app() :

    
    # 사이드 메뉴

    radio_menu = ['Bar', 'dia']
    selected_radio = st.sidebar.radio("Distribution", radio_menu)

    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')

    if selected_radio == 'Bar' :
        st.title('Bar Chart')
        st.write(' 지역별 리뷰 수 ')
    

        fig1 = plt.figure()
        df['province'].hist()
        st.pyplot(fig1)
        

    elif selected_radio == 'dia':
        st.write('--')

