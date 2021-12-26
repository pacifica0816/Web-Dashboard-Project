import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
   
def run_search_app() :

    radio_menu = ['Taster', 'Wine']
    selected_radio = st.sidebar.radio("검색할 종류를 선택하세요.", radio_menu)

    if selected_radio == 'Taster' :
        st.title('Tatser Search')
        

        st.subheader('테이스터 검색')

        df = pd.read_csv('data/winemag.csv', index_col=0)
        df.dropna(axis=0, inplace=True)
        df.to_csv('data/winemag.csv')


        # 이름 검색
        word = st.text_input('이름을 입력하세요.')
        word = word.lower()
        df_search = df.loc[ df['taster_name'].str.lower().str.contains(word) , ]
        df['taster_name'].unique
        st.dataframe( df_search )



    elif selected_radio == 'Wine':
        st.title('Title Search')

        # 와인 이름 검색
        st.subheader('키워드를 입력해 와인 검색')

        df = pd.read_csv('data/winemag.csv', index_col=0)
        df.dropna(axis=0, inplace=True)
        df.to_csv('data/winemag.csv')

        word2 = st.text_input('예) sweet, noir, 2012')
        word2 = word2.lower()
        df_search = df.loc[ df['title'].str.lower().str.contains(word2) , ]
        df['title'].unique
        st.dataframe( df_search )

        




