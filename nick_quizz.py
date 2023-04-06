import streamlit as st

st.title('Пройди тест и узнай, какой ты мультик :orange[Nickelodeon]:tada:')

st.markdown("Привет! Это наш :orange[**проект**]. Пройди тест, будет весело!:star-struck:")

# словарь для подсчета очков результата
dict_fin = {
             'ГБ': 0, 'КП': 0, 'КБ': 0, "ОУЭД": 0, "ДП": 0, "ЭА": 0, "ДН": 0, "ПИМ": 0, "РИК": 0
            }

# словарь ответов и результатов вопроса 1
dict_1 = {'Они думали, мы упадём океанами стали, мне это нравится, нравится.': 'ГБ',
          'Я — это ты, ты — это я, и никого не надо нам.': 'КП',
          'Плыл по пруду барабан, был барабан бобром замечен, жизнь бобра менять пора, так решил он в этот вечер.': 'КБ',
          'Девочки и мальчики, сладкие, как карамельки, а на них большие башмаки, это барбарики.': 'ОУЭД',
          'Мы убежим - нас не догонят. Дальше от них, дальше от дома!': 'ДП',
          'Если спросят меня, где взяла я такого мальчишку сладкого, я отвечу, что угнала...': 'ЭА',
          'Ты первый в биткоин сделал вложения, для microsoft писал дополнения, так меня манят твой ум и стремления и моноколёсный скутер с сидением.': 'ДН',
          'Зачем мне солнце Монако, для чего скажи мне луна Сен Тропе?': 'ПИМ',
          'Едем, едем в соседнее село на дискотеку! Едем, едем на дискотеку со своей фонотекой.': 'РИК'}
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# вопрос 1
option_1 = st.radio(
    (st.markdown('<p class="big-font">Какие строчки заставляют ваше сердце биться чаще?</p>', unsafe_allow_html=True)),
    ('Они думали, мы упадём океанами стали, мне это нравится, нравится.', 'Я — это ты, ты — это я, и никого не надо нам.', 
     'Плыл по пруду барабан, был барабан бобром замечен, жизнь бобра менять пора, так решил он в этот вечер.', 
     'Девочки и мальчики, сладкие, как карамельки, а на них большие башмаки, это барбарики.', 'Мы убежим - нас не догонят. Дальше от них, дальше от дома!', 
     'Если спросят меня, где взяла я такого мальчишку сладкого, я отвечу, что угнала...', 
     'Ты первый в биткоин сделал вложения, для microsoft писал дополнения, так меня манят твой ум и стремления и моноколёсный скутер с сидением.', 
     'Зачем мне солнце Монако, для чего скажи мне луна Сен Тропе?', 'Едем, едем в соседнее село на дискотеку! Едем, едем на дискотеку со своей фонотекой.'))

# учет результата
res_1 = dict_1[option_1]
dict_fin[res_1] =+ 1
