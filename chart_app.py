import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart_app() :

    
    side_menu = ['Bar', 'Map']
    side_box = st.sidebar.selectbox("Distribution", ("Bar", " Map"))

    if side_menu == 'Bar' :
       
        st.title('바차트')
        
        radio_menu = ['Country','Province','Price']
        selected_radio = st.radio('Visualization : ', radio_menu)

        # if selected_radio == 'Bar' :
        #     st.write('바차트')
        # elif selected_radio == 'Map' :
        #     st.write('맵~')
        
    elif side_menu == 'Map' :
        st.title('맵')






    # b = (
    #     Bar()
    #     .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    #     .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
    #         ),
    #         toolbox_opts=opts.ToolboxOpts(),
    #     )
    # )
    # st_pyecharts(
    #     b, key="echarts"
    # )  # Add key argument to not remount component at every Streamlit run
    # st.button("Randomize data")
