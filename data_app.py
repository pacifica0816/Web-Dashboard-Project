import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser
   
def run_data_app() :

    df = pd.read_csv('data/winemag.csv', index_col=0)
    df.dropna(axis=0, inplace=True)
    df.to_csv('data/winemag.csv')


    st.subheader('최고 점수를 받은 와인')
    st.image('data/wine1.jpg')
    st.dataframe( df.loc[ df['points'] == df['points'].max(), 'title'] )

    if st.checkbox("info"):
        st.dataframe( df.loc[ df['points'] == df['points'].max(), ])
        if st.button('Google Maps') :
            url = 'https://www.google.com/search?q=charles%20smith%20winery&sxsrf=AOaemvK_K0fqaBFgOVIt6sn4poWAdIlQOw:1640544019058&ei=D7fIYZf0IJrM-QaHz464Dg&oq=Charles+Smith+%E3%85%88&gs_lcp=Cgdnd3Mtd2l6EAMYATIFCAAQgAQyCggAEIAEEIcCEBQyBQgAEIAEOgcIIxCwAxAnOgkIABCwAxAHEB46CAgAEIAEELADOgQIIxAnOgoILhCABBCHAhAUSgQIQRgBSgQIRhgAUN8CWJQLYOYSaAFwAHgAgAGkAYgB5AOSAQMwLjSYAQCgAQHIAQrAAQE&sclient=gws-wiz&tbs=lf:1,lf_ui:10&tbm=lcl&rflfq=1&num=10&rldimm=7107699294120712506&lqi=ChRjaGFybGVzIHNtaXRoIHdpbmVyeRnIDmk7SebOHkiUi5PIgJiAgAhaJBAAEAEQAhgBGAIiFGNoYXJsZXMgc21pdGggd2luZXJ5MgJlbpIBCHdpbmVfYmFymgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVJ6Tms5ZlluVkJSUkFCqgEmCggvbS8wODFxYxABKhgiFGNoYXJsZXMgc21pdGggd2luZXJ5KAA&phdesc=KXJr1rYazno&ved=2ahUKEwil1fnbjoL1AhWUd94KHRJjDVsQvS56BAgpEDI&rlst=f#rlfi=hd:;si:7107699294120712506,l,ChRjaGFybGVzIHNtaXRoIHdpbmVyeRnIDmk7SebOHkiUi5PIgJiAgAhaJBAAEAEQAhgBGAIiFGNoYXJsZXMgc21pdGggd2luZXJ5MgJlbpIBCHdpbmVfYmFymgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVJ6Tms5ZlluVkJSUkFCqgEmCggvbS8wODFxYxABKhgiFGNoYXJsZXMgc21pdGggd2luZXJ5KAA,y,KXJr1rYazno;mv:[[47.6350848,-118.0959852],[45.9794396,-122.55604220000001]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10'
            webbrowser.open_new_tab(url)
        else :
            pass
    else :
        pass
    st.header(' ')
    st.header(' ')

    st.subheader('가격대비 평점이 가장 좋은 와인')
    st.image('data/best.png')
    df_eco = df['points'] / df['price']
    df_eco == df_eco.max()
    st.dataframe( df.loc[ df_eco == df_eco.max(), 'title' ] )

    if st.checkbox("info."):
        st.dataframe( df.loc[ df_eco == df_eco.max(), ])
        if st.button('Google Maps.') :
            url = 'https://www.google.com/search?q=california+winery&tbm=lcl&sxsrf=AOaemvKDR4HStqWpeARnhFBfTo0tSWudtQ%3A1640544195403&ei=w7fIYeH9F_CumAWfrq6ICw&oq=california+winery&gs_l=psy-ab.3..0i7i30k1l4j0i512k1l2j0i7i30k1l4.365451.381341.0.381546.23.18.5.0.0.0.161.1970.0j15.15.0....0...1c.1j4.64.psy-ab..3.17.1744...0i10i19i42k1j0i13i10i30i19k1j0i67k1j0i13k1j0i7i30i19k1.0.IOVLlFlI-kQ#rlfi=hd:;si:3971736969081389893,l,ChFjYWxpZm9ybmlhIHdpbmVyeUjqueeA5oCAgAhaIRABGAAYASIRY2FsaWZvcm5pYSB3aW5lcnkqAggDMgJlbpIBBndpbmVyeaoBDhABKgoiBndpbmVyeSgA,y,UM33yeSH5rs;mv:[[39.5934787,-120.06679849999999],[34.610247199999996,-123.67548449999998]]'
            webbrowser.open_new_tab(url)
            st.write('')
        else :
            pass
    else :
        pass
    st.header(' ')
    st.header(' ')


    st.subheader('최저 점수를 받은 와인')
    st.dataframe( df.loc[ df['points'] == df['points'].min(), 'title' ])

    if st.checkbox("info.."):
        st.dataframe( df.loc[ df['points'] == df['points'].min(), ])
    else :
        pass
    st.header(' ')
    st.header(' ')

    st.subheader('평가 점수와 가격 평균')
    st.dataframe(df.describe())
    st.header(' ')
    st.header(' ')

    # 컬럼별 데이터 보여주기
    selected_columns = st.multiselect('항목을 선택하세요.', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe( df[selected_columns] )
    else :
        pass
 



