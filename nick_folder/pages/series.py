import streamlit as st
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from cartoons import question
question(5)
st.title('Здесь тест по сериалам')
