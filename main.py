import streamlit as st
import folium
from streamlit_folium import st_folium

# --- 페이지 설정 ---
st.set_page_config(page_title="이집트 여행 가이드", layout="wide")

# --- 제목 ---
st.title("🕌 이집트 여행지 가이드")
st.markdown("이집트의 대표적인 여행지를 알아보고, 지도에서 직접 위치도 확인해보세요!")

# --- 여행지 데이터 ---
destinations = [
    {
        "name": "카이로 (Cairo)",
        "description": "이집트의 수도이자 고대 이집트 문명의 중심지. 기자의 피라미드, 이집트 박물관이 위치해 있습니다.",
        "lat": 30.0444,
        "lon": 31.2357
    },
    {
        "name": "룩소르 (Luxor)",
        "description": "고대 테베로 불렸던 도시. 카르낙 신전, 룩소르 신전, 왕가의 계곡 등 유적이
