import os, sys
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd
from PIL import Image
import random
from pathlib import Path

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from cartoons import question, count_result

# словарь для подсчета очков результата
dict_fin = {
    'ДЖ': 0, 'ДЧ': 0, "ЖЗК": 0, "ВВП": 0, "ХМ": 0
}
data = pd.read_csv(os.path.join(os.path.dirname(__file__), '../question_series.csv'), sep=";", on_bad_lines='skip')

# код страницы
st.title("Пройди тест и узнай, какой ты сериал :purple[Disney]:tada:")

go_back = st.button(":purple[**Вернуться назад**]")
if go_back:
    switch_page("main code")

list_of_users_answers = question(5)

res_button = st.button(":purple[**Узнать результаты**]")
if res_button:
    users_result = count_result(list_of_users_answers)
    st.session_state['users_result_series'] = users_result
    switch_page("result_series")
