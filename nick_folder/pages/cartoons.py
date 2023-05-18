import os
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd
from PIL import Image
import random
from pathlib import Path


# словарь для подсчета очков результата
dict_fin = {
    'ГБ': 0, 'КБ': 0, "ДП": 0, "ЭА": 0, "ДН": 0
}

data = pd.read_csv(os.path.join(os.path.dirname(__file__), '../question_data.csv'), sep=";", on_bad_lines='skip')

# data = pd.read_csv('https://gitlab.com/ddariath/nick_data/-/raw/main/question_data.csv', sep=";", on_bad_lines='skip')


def question(amount):  # получает на вход количество вариантов ответа для вопросов: 5
    global data
    st.session_state['option'] = []
    # user_answ = []
    for quest_num in range(1, 10):

        que = data['answer'].iloc[[6 * quest_num - 6]].values[0]

        # вывод вопроса-картинки
        if 'png' in que:
            file_name = Path(que)
            st.image(Image.open(os.path.join(os.path.dirname(__file__), file_name)))

        # вывод текстового вопроса
        else:
            st.markdown(que)

        # список вариантов ответов
        start = (amount + 1) * quest_num - amount
        end = (amount + 1) * quest_num - 1
        answers = data['answer'].loc[start:end].tolist()

        # вывод вариантов ответа
        current_question_option = st.radio("скрытый текст вопроса", answers, label_visibility="collapsed")

        # добавление ответа пользователя в session state
        if current_question_option:
            st.session_state['option'].append(current_question_option)

    user_answ = st.session_state['option']
    # st.write(user_answ)  # проверка вывода

    return user_answ


def count_result(list_of_answers):
    global data
    global dict_fin

    # учет ответов пользователя
    for answer in list_of_answers:
        user_result = data['result'].iloc[data.index[data['answer'] == answer]].to_string(index=False)
        dict_fin[user_result] += 1


    # поиск результата с максимальным значением
    list_fin = dict_fin.values()
    res_fin = max(list_fin)

    # поиск ключа по максимальному значению
    res_list = []
    for key, value in dict_fin.items():
        if res_fin == value:
            res_list.append(key)

    # выбор результата при одинаковых значениях
    if len(res_list) > 1:
        result = random.choice(res_list)
    else:
        result = res_list[0]

    return result


data_res = pd.read_csv(os.path.join(os.path.dirname(__file__), '../result_data.csv'), sep=";", on_bad_lines='skip')


def print_result(res):
    i_res = data_res.index[data_res['Result'] == res]
    name_result = data_res['Full_name'].iloc[i_res].values[0]
    st.title(f'Ваш результат - :orange[{name_result}]')
    text_result = data_res['Text'].iloc[i_res].values[0]
    st.subheader(text_result)
    image_result = data_res['Image'].iloc[i_res].values[0]
    st.text(image_result)
    image_name = Path(image_result)
    st.image(Image.open(os.path.join(os.path.dirname(__file__), image_name)))

st.title("Пройди тест и узнай, какой ты мультик :orange[Nickelodeon]:tada:")

go_back = st.button(":orange[**Вернуться назад**]")
if go_back:
    switch_page("main code")

list_of_users_answers = question(5)

res_button = st.button(":orange[**Узнать результаты**]")
if res_button:
    users_result = count_result(list_of_users_answers)
    #print_result(users_result)
    switch_page("result_cartoons")
