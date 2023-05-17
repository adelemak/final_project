import streamlit as st
import pandas as pd
from pages.cartoons import dict_fin, users_result  # dict_fin - для проверки словаря результатов,
                                                   # users_result - результат пользователя
import os
from cartoons.py import count_result


data = pd.read_csv(os.path.join(os.path.dirname(__file__), '../question_data.csv'), sep=";", on_bad_lines='skip')



data_res = pd.read_csv(os.path.join(os.path.dirname(__file__), '../result_data.csv'), sep=";", on_bad_lines='skip')


def print_result(res):
    i_res = data_res.index[data_res['Result'] == res]
    name_result = data_res['Full_name'].iloc[i_res].values[0]
    st.title(f'Ваш результат - {name_result}')
    text_result = data_res['Text'].iloc[i_res].values[0]
    st.subheader(text_result)

#st.write(users_result) - не передается
st.write(dict_fin)  # для проверки
st.write(dict_of_users_answers)
#print_result(users_result)
