import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 웹페이지 기본 설정
st.set_page_config(page_title="내가 좋아하는 여행지", layout="centered")

# 제목
st.title("🌍 내가 좋아하는 여행지 소개")

# 여행지 리스트
places = {
    "파리 (프랑스)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg",
        "description": "에펠탑, 루브르 박물관, 세느강이 아름다운 예술과 낭만의 도시 파리!",
        "coordinates": (48.8566, 2.3522),
        "video": "https://www.youtube.com/watch?v=8ZqDOk8U_9I"
    },
    "교토 (일본)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Kiyomizu-dera_in_Kyoto%2C_Japan.jpg",
        "description": "전통과 자연이 어우

