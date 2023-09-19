import streamlit as st
import streamlit_antd_components as sac
import labeler


with st.sidebar.container():
    selection = sac.menu([
        sac.MenuItem('GPT Labeler', icon='incognito')
    ])
    

pages = {'GPT Labeler': labeler}

page = pages[selection]
page.main(selection)