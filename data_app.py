import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
   
def run_data_app() :

    st.subheader('data 화면입니다.')

    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')
    pd.options.display.float_format = '{:.2f}'.format
    st.dataframe(df)


    # 컬럼별 데이터 보여주기

    selected_columns = st.multiselect('컬럼을 선택하세요', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe( df[selected_columns] )
    else :
        st.write('선택한 컬럼이 없습니다.')


    # 사이드 메뉴에 표시될 글씨
    st.sidebar.header('원하는 옵션을 선택하세요.')


    # country_parties = df_country['US'].unique().tolist()
    # country_party_selected = st.sidebar.multiselect('country parties', pol_parties, pol_parties)
    # nb_deputies = df_dep['pol party'].value_counts()
    # nb_mbrs = st.sidebar.slider("Number of members", int(nb_deputies.min()), int(nb_deputies.max()), (int(nb_deputies.min()), int(nb_deputies.max())), 1)


    # # 사이드바 셀렉트 위젯
    # mask_pol_par = df_dep['pol party'].isin(pol_party_selected)
    
    # # 배열의 멤버수 파티로 묶기
    # mask_mbrs = df_dep['pol party'].value_counts().between(nb_mbrs[0], nb_mbrs[1]).to_frame()
    # mask_mbrs= mask_mbrs[mask_mbrs['pol party'] == 1].index.to_list()
    # mask_mbrs= df_dep['pol party'].isin(mask_mbrs)
    # df_dep_filtered = df_dep[mask_pol_par & mask_mbrs]
    # st.write(df_dep_filtered)


## 데이터프레임 메뉴
    # 컬럼명 한글로 바꾸기 > 되나?
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
