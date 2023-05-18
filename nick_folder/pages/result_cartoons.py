import streamlit as st
import pandas as pd
import os
from pathlib import Path
from PIL import Image

users_result = st.session_state['users_result']

data_res = pd.read_csv(os.path.join(os.path.dirname(__file__), '../result_data.csv'), sep=";", on_bad_lines='skip')


def print_result(res):
    i_res = data_res.index[data_res['Result'] == res]
    name_result = data_res['Full_name'].iloc[i_res].values[0]
    st.title(f'Ваш результат - :orange[{name_result}]')
    image_result = data_res['Image'].iloc[i_res].values[0]
    image_name = Path(image_result)
    st.image(Image.open(os.path.join(os.path.dirname(__file__), image_name)))
    text_result = data_res['Text'].iloc[i_res].values[0]
    st.subheader(text_result)

st.baloons()
print_result(users_result)
