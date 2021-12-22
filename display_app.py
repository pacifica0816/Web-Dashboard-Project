import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
   
def run_display_app() :

    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')
    pd.options.display.float_format = '{:.2f}'.format

    # 컬럼별 데이터 보여주기
    selected_columns = st.multiselect('표시할 항목들을 선택하세요', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe( df[selected_columns] )
    else :
        st.write('선택한 컬럼이 없습니다.')


