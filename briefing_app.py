import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
   
def run_briefing_app() :

    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')
    pd.options.display.float_format = '{:.2f}'.format




    # 가성비
    st.subheader('가격대비 평점이 가장 좋은 와인')
    df_eco = df['points'] / df['price']
    df_eco == df_eco.max()
    st.dataframe( df.loc[ df_eco == df_eco.max(), 'title' ] )

    
    st.subheader('평가 점수와 가격 평균')
    st.dataframe(df.describe())
    

    # st.subheader('최고 점수를 받은 와인')
    # st.dataframe( df.loc[ df['points'].max(), 'title'] )


