import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random
from data_app import run_data_app


def main() :

    menu = ['Home','Data', 'Display']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home' :
        st.title('소믈리에의 와인 리뷰')
        st.write('좋은 평을 받은 와인을 알아보기!')
    elif choice == 'Data' :
        run_data_app()

    
if __name__ == '__main__' :
    main()