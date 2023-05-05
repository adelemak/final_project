import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd


#data = pd.read_csv('https://raw.githubusercontent.com/adelemak/final_project/main/nick_data.csv?token=GHSAT0AAAAAACA56NSLR2RH366AS3KZIRLOZBZNQLQ',
 #                  sep=";", on_bad_lines='skip')

# словарь для подсчета очков результата
dict_fin = {
             'ГБ': 0, 'КП': 0, 'КБ': 0, "ОУЭД": 0, "ДП": 0, "ЭА": 0, "ДН": 0, "ПИМ": 0, "РИК": 0
            }

def question(amount):  # получает на вход количество вариантов ответа для вопросов: 4 или 9

    data = pd.read_csv('https://raw.githubusercontent.com/adelemak/final_project/main/nick_data.csv?token=GHSAT0AAAAAACA56NSLR2RH366AS3KZIRLOZBZNQLQ',
        sep=";", on_bad_lines='skip')
    for num in range(1, amount + 1):

        que = data['answer'].iloc[[10 * num - 10]]
        que_str = que.to_string(index=False)

        start = 10 * num - 9
        end = 10 * num - 1
        answ = data['answer'].loc[start:end].tolist()

        st.markdown(que_str)
        option = st.radio("скрытый текст вопроса", answ, label_visibility="collapsed")

        user_result = data['result'].iloc[[data.index[data['answer'] == option]]]
        global dict_fin
        dict_fin[user_result] = + 1


st.title("Пройди тест и узнай, какой ты мультик :orange[Nickelodeon]:tada:")

go_back = st.button(":orange[**Вернуться назад**]")
if go_back:
    switch_page("main code")

quest_button = st.button(":orange[**Начать тест**]")
if quest_button:
    question(9)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**2. Выберите картинку**")
    option_3 = st.radio("Выберите картинку", ("1", "2", "3"), label_visibility = "collapsed")
with col2:
    st.text("1.")
    st.image("https://github.com/adelemak/final_project/blob/fd27c51306d3e2a33c7dec0dfef607cf6b2526f1/nick_folder/pictures/Arnold.webp", width=200)
    st.text("2.")
    st.image("https://rg.ru/uploads/images/193/20/18/medved.jpg", width=200)
    st.image("https://media0.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif?cid=ecf05e47ac8960707e6e75ad6b8e0d8c3ca0e061d7774ce1&rid=giphy.gif&ct=g")
