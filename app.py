import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random



def main() :
    menu = ['', 'CSV', 'About']
    st.title('와인리뷰를 알아보자!')
    st.text('쉬라 존맛이라네용 :3')

    st.info('신도림 엉베흐 존맛턍인거 다들아시죠? 존맛입니다')



    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')
    pd.options.display.float_format = '{:.2f}'.format
    st.dataframe(df)
    






if __name__ == '__main__' :
    main()