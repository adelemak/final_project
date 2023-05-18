import streamlit as st
import pandas as pd
import os, sys
from pathlib import Path
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from result_cartoons import print_result

users_result = st.session_state['users_result_series']

data_res = pd.read_csv(os.path.join(os.path.dirname(__file__), '../result_series.csv'), sep=";", on_bad_lines='skip')

st.balloons()
print_result(users_result)

start_test_again = st.button(":purple[**Пройти тест снова**]:rocket:")
if start_test_again:
    switch_page("series")

go_to_main = st.button(":purple[**Вернуться на главную**]:taxi:")
if go_to_main:
    switch_page("main code")
