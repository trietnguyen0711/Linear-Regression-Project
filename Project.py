import streamlit as st
import numpy as np
import pickle
with open('model.pickle', 'rb') as f:
  linearModel = pickle.load(f)
st.title('Sales Prediction')
value1 = st.number_input('TV')
value2 = st.number_input('Radio')
if st.button('Predict Sales'):
  x = np.array([[value1,value2]])
  result = linearModel.predict(x)
  st.write(f'Predict sales : {np.round(result[0],2)}')


