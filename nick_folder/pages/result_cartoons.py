import streamlit as st
import pandas as pd
import os
from pathlib import Path
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

users_result = st.session_state['users_result_cartoons']

data_res = pd.read_csv(os.path.join(os.path.dirname(__file__), '../result_data.csv'), sep=";", on_bad_lines='skip')


def print_result(res):
    i_res = data_res.index[data_res['Result'] == res]
    name_result = data_res['Full_name'].iloc[i_res].values[0]
    st.title(f'Ваш результат - :orange[{name_result}]:tada:')
    image_result = data_res['Image'].iloc[i_res].values[0]
    image_name = Path(image_result)
    st.image(Image.open(os.path.join(os.path.dirname(__file__), image_name)))
    text_result = data_res['Text'].iloc[i_res].values[0]
    st.subheader(text_result)

st.balloons()
print_result(users_result)

col_var, col_var2 = st.columns(2)

with col_var:
    start_test_again = st.button(":rocket: :orange[**Пройти тест снова**]")
    if start_test_again:
        switch_page("cartoons")
with col_var2:
    go_to_main = st.button(":taxi: :orange[**Вернуться на главную**]")
    if go_to_main:
        switch_page("main code")
