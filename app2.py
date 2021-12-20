import streamlit as st
import pandas as pd
    if status == '오름차순 정렬' :
        st.dataframe( df.sort_values('petal_length') )
    elif status == '내림차순 정렬' :
        st.dataframe( df.sort_values('petal_length', ascending=False) )
        

    language = ['Python', 'C', 'Java', 'Go']
    my_choice = st.selectbox('좋아하는 언어를 선택하세요', language)
    if my_choice == 'C' :
        st.write('저는 C가 좋아요')
    elif my_choice == 'Python' : 
        st.write('팥붕이 최고다.')
