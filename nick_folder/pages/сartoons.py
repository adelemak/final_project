import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd



# словарь для подсчета очков результата
dict_fin = {
             'ГБ': 0, 'КБ': 0, "ДП": 0, "ЭА": 0, "ДН": 0
            }

def question(amount):  # получает на вход количество вариантов ответа для вопросов: 5

    data = pd.read_csv('https://gitlab.com/ddariath/nick_data/-/raw/main/question_data.csv', sep=";", on_bad_lines='skip')
    user_answ = []
    for quest_num in range (1, 9):
        que = data['answer'].iloc[[6 * quest_num - 6]]
        que_str = que.to_string(index=False)
        
        start = (amount + 1) * quest_num - amount
        end = (amount + 1) * quest_num - 1
        answ = data['answer'].loc[start:end].tolist()

        st.markdown(que_str)
        option = st.radio("скрытый текст вопроса", answ, label_visibility="collapsed")
        user_answ.append(option)
        #user_result = data['result'].iloc[[data.index[data['answer'] == option]]]
        #global dict_fin
        #dict_fin[user_result] = + 1
    return user_answ
        
def count_result(list_of answers):
    #учет ответов пользователя  
    for answer in  list_of_answers:
        user_result = data['result'].iloc[[data.index[data['answer'] == option]]]
        global dict_fin
        dict_fin[user_result] = + 1
    
    # поиск результата с максимальным значением
    list_fin = dict_fin.values()
    res_fin = max(list_fin)
    res_list = []
    
    # поиск ключа по максимальному значению
    for key, value in dict_fin.items():
        if res_fin == value:
            res_list.append(key)
            
    # выбор результата при одинаковых значениях
    if len(res_list) > 1:
        result = random.choice(res_list)
    else:
        result = res_list[0]
    
    return result

st.title("Пройди тест и узнай, какой ты мультик :orange[Nickelodeon]:tada:")

go_back = st.button(":orange[**Вернуться назад**]")
if go_back:
    switch_page("main code")

question(5)
count_result(question(amount))
    
res_button = st.button("Узнать результаты")
if res_button:
    switch_page("result")
