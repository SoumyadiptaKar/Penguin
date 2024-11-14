import streamlit as st
import pandas as pd
st.title('🐧 Machine Learning App')

st.info('This is a machine learning app.')

with st.expander('Data'):
  st.write('Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**y**')
  y=df.species
  y

with st.expacder('Data Visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df, *, x='bill_length_mm', y='body_mass_g', x_label=None, y_label=None, color='species')
