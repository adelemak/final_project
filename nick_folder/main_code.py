import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from streamlit_extras.let_it_rain import rain
import os

rain(
    emoji="🍭",
    font_size=30,
    falling_speed=5,
    animation_length="1",
)

st.title('Добро пожаловать на страничку с :green[тестами]:tada:')

st.markdown("Привет! Это наш :orange[**проект**]. Здесь ты можешь выбрать один из тестов и пройти его, можешь пройти оба, они интересные!")

st.markdown('Будет весело!:star-struck:')


col_test1, col_test2 = st.columns(2)
with col_test1:
    switch1 = st.button(":clapper: :violet[**Тест по сериалам**]")
    if switch1:
        switch_page("series")
with col_test2:
    switch2 = st.button(":rainbow: :orange[**Тест по мультикам**]")
    if switch2:
        switch_page("cartoons")


card(title="Quiz",text=":)", image="https://vejasp.abril.com.br/wp-content/uploads/2016/12/nickelodeon.jpg")
