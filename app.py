import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random
from search_app import run_search_app
from data_app import run_data_app
from chart_app import run_chart_app


def main() :
    st.sidebar.header('Menu')
    menu = ['Home','Search', 'Data', 'Chart']
    choice = st.sidebar.selectbox('Choose your preferred display:', menu)

    if choice == 'Home' :
        st.title('Wine reviewed by world tasters.')
        st.write('유명 테이스터들이 평가한 와인 데이터를 분석한 앱입니다.')
        st.image('data/wine.gif')


    elif choice == 'Search' :
        run_search_app()
    elif choice == 'Data' :
        run_data_app()
    elif choice == 'Chart' :
        run_chart_app()



if __name__ == '__main__' :
    main()