import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
   
def run_data_app() :

    st.subheader('소믈리에를 검색하세요.')


    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')
    pd.options.display.float_format = '{:.2f}'.format
    # st.dataframe(df)

    # 1. 유저한테 검색어 입력을 받습니다.
    word = st.text_input('이름을 입력하세요.')
    print(word)
    word = word.lower()
    # 2. 검색어를 데이터프레임의 taster_name 컬럼에서 검색해서
    # 가져온다.
    df_search = df.loc[ df['taster_name'].str.lower().str.contains(word) , ]
    df['taster_name'].unique

    # 3. 화면에 결과를 보여준다.
    # st.dataframe( df_search )

    # 사이드 메뉴에 표시될 글씨
    st.sidebar.subheader('Options')

## 데이터프레임 메뉴
    # 와인이름컬럼 '검색'기능
    # 지역별 카테고리
    # 가격별 카테고리
    # 가격대비 높은 평점 보여주기
    # 평점순 정렬

## 시각화 메뉴
    # 지역별 그래프
    # 나라별 그래프
    # 양조장별 그래프
    # 포인트별 그래프
    # 가격대별 그래프
