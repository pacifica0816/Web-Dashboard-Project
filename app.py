import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random



def main() :
    st.title('최고의 와인을 알아보자!')
    st.text('쉬라 존맛이라네용 :3')

    st.info('신도림 엉베흐 존맛턍인거 다들아시죠? 존맛입니다')

    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')
    st.dataframe(df)
    
    # '{:.2f}'.format
    # choice_list = st.multiselect("여러개를 선택할 수 있습니다.", language)


if __name__ == '__main__' :
    main()