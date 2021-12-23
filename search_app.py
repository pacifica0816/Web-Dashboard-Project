import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
   
def run_search_app() :

    radio_menu = ['Taster', 'Wine']
    selected_radio = st.sidebar.radio("검색할 종류를 선택하세요.", radio_menu)

    if selected_radio == 'Taster' :
        st.title('Bar Chart')
        

        st.subheader('테이스터 검색')


        df = pd.read_csv('data/winemag.csv', index_col=0)
        df.dropna(axis=0, inplace=True)
        df.to_csv('data/winemag.csv')
        pd.options.display.float_format = '{:.2f}'.format


        # 이름 검색
        word = st.text_input('테이스터 이름을 입력하세요.')
        word = word.lower()
        df_search = df.loc[ df['taster_name'].str.lower().str.contains(word) , ]
        df['taster_name'].unique
        st.dataframe( df_search)



    elif selected_radio == 'Wine':
        st.write('--')

        # 와인 이름 검색
        st.subheader(' ')
        st.subheader('키워드를 입력해 와인 검색')

        word2 = st.text_input('예) sweet, noir')
        word2 = word2.lower()
        df_search = df.loc[ df['title'].str.lower().str.contains(word2) , ]
        df['title'].unique
        st.dataframe( df_search )

        

    # 컬럼별 데이터 보여주기
    selected_columns = st.multiselect('항목을 선택하세요.', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe( df[selected_columns] )
    else :
        pass


    if st.button("button"):
        pass




## 데이터프레임 메뉴
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
