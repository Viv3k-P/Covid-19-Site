import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from getData import run

from main import d
#from main import prov
d = run()
prov = ["BC","AB","SAS","MA","ON","QB","NL","NB","NS","PEI","YK","NW","NUN"]

st.set_page_config(page_title='TEST')
st.header('COVID-19 Ontario')
st.subheader('Cases by prov')


# z = {'prov': prov, 'cases' : [560, 531, 271, 102, 328, 342, 0, 50, 6, 3, 9, 56, 0]}

z = {'prov': prov, 'cases' : [560, 531, 271, 102, 328, 342, 0, 50, 6, 3, 9, 56, 0]}
df_prov_cases = pd.DataFrame(d)
# st.dataframe(df_prov_cases)



print(d['cases'],d['prov'])
bar_chart = px.bar(df_prov_cases,x='prov',y='cases')#,template='plotly_white',color_discrete_sequence=['#F63366']*len(df_prov_cases))
st.plotly_chart(bar_chart)
# st.subheader('aksdjfklas')