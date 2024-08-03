# -*- coding: utf-8 -*-
"""activity4_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-oFV9qIAvVgy5B6UoYxC-6a0VbGF1ydb
"""

import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Diabetes Data')
df = pd.read_csv('https://storage.googleapis.com/scsu-data-science/diabetes_nan.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Diabetic vs Non-DDiabetic')

outcome = st.radio('Select outcome', ('Diabetic', 'Non-Diabetic'))

if origin == 'Diabetic':
    df = df.loc[df['Outcome']=='1']
else:
    df = df.loc[df['Outcome']=='0']

fig = sns.figure()
ax = fig.add_subplot()
ax.set_xlabel('Frequency')
ax.hist(df['Frequency'])
st.sns(fig)
