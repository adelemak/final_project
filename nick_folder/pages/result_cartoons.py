import streamlit as st
import pandas as pd
from pages.cartoons import dict_fin, users_result, list_of_users_answers  # dict_fin - для проверки словаря результатов,
                                                   # users_result - результат пользователя
import os
from cartoons import count_result, question


data = pd.read_csv(os.path.join(os.path.dirname(__file__), '../question_data.csv'), sep=";", on_bad_lines='skip')



data_res = pd.read_csv(os.path.join(os.path.dirname(__file__), '../result_data.csv'), sep=";", on_bad_lines='skip')


def print_result(res):
    i_res = data_res.index[data_res['Result'] == res]
    name_result = data_res['Full_name'].iloc[i_res].values[0]
    st.title(f'Ваш результат - :orange[{name_result}]:')
    text_result = data_res['Text'].iloc[i_res].values[0]
    st.subheader(text_result)
    image_result = data_res['Image'].iloc[i_res].values[0]
    image_name = Path(image_result)
    st.image(Image.open(os.path.join(os.path.dirname(__file__), image_name)))

print_result(users_result)
#st.write(users_result) - не передается
st.write(dict_fin)  # для проверки
st.write(dict_of_users_answers)

