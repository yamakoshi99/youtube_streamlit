import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

st.title('streamlit 超入門')

st.write('Display Image')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
ber = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{1+i}')
    ber.progress(i + 1)
    time.sleep(0.01)

'Done!!!'





st.write('Interactive widgts')

expander = st.beta_expander('お問合せ')
expander.write('お問合せをかく')


text = st.text_input('あなたの趣味を教えてください')
'あなたの好きな趣味は', text , 'です'
text = st.slider('あなたの今の調子は？',0,100,50)
'コンディション',text

if (st.checkbox('Show Image')):
    img = Image.open('sample.JPG')
    st.image(img, caption='takuya' , use_column_width=True)
