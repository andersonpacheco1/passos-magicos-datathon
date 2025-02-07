import streamlit as st

st.set_page_config(layout="wide")

pages = {
    'Contextualização':[
        st.Page('contexto.py', title='Contexto', icon=':material/topic:')
    ],
    'Análises':[
    # st.Page('analitica.py', title='Analítica', default=True, icon=':material/candlestick_chart:'),
    st.Page('preditiva.py', title='Preditiva', icon=':material/polyline:')
]}

pg = st.navigation(pages)
pg.run()