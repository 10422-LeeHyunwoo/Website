import streamlit as st
import folium
from streamlit_folium import st_folium
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="이집트 모험 여행 가이드", layout="wide")

# --- 제목 및 소개 ---
st.markdown("<h1 style='text-align: center;'>🧳 ✨ 이집트 모험 여행 가이드 ✨ 🧳</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>고대의 신비를 품은 이집트로 떠나는 상상 여행!<br>지도로 즐기고, 설명도 읽고, 랜덤 추천도 받아보세요 🎒</p>", unsafe_allow_html=True)
st.divider()

# --- 여행지 데이터 ---
destinations = [
    {
        "name": "카이로 (Cairo)",
        "description": "🛕 <b>이집트의 수도이자 문명의 중심</b><br>이집트 박물관, 기자의 피라미드 등 상징적인 유적이 많습니다.",
        "lat": 30.0444,
        "lon": 31.2357,
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Kheops-Pyramid.jpg"
    },
    {
        "name": "룩소르 (Luxor)",
        "description": "🏺 <b>고대 테베의 중심지</b><br>카르낙 신전, 룩소르 신전, 왕가의 계곡이 있는 유적지 천국입니다.",
        "lat": 25.6872,
        "lon": 32.6396,
        "img": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Karnak_Temple.jpg"
    },
    {
        "name": "아스완 (Aswan)",
        "description": "🌅 <b>나일강의 낭만 도시</b><br>필레 신전과 아부심벨 신전이 유명하며, 평화로운 분위기가 매력적입니다.",
        "lat": 24.0889,
        "lon": 32.8998,
        "img": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Philae_Temple.jpg"
    },
    {
        "name": "샤름엘셰이크 (Sharm El-Sheikh)",
        "description": "🌊 <b>홍해의 리조트 천국</b><br>스노클링, 다이빙, 선셋 크루즈 등 액티비티 가득한 해변 도시입니다.",
        "lat": 27.9158,
        "lon": 34.3290,
        "img": "https://upload.wikimedia.org/wikipedia/commons/4/41/Sharm_el-Sheikh_Beach.jpg"
    },
    {
        "name": "알렉산드리아 (Alexandria)",
        "description": "🏛️ <b>알렉산더 대왕의 도시</b><br>고대 도서관의 전설이 남아 있으며, 지중해의 매력을 느낄 수 있습니다.",
        "lat": 31.2001,
        "lon": 29.9187,
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Citadel_of_Qaitbay_%28Alexandria%29.jpg"
    }
]

# --- 사이드바 ---
st.sidebar.header("📍 여행지 탐색기")
selected = st.sidebar.selectbox("🔎 여행지를 선택하세요:", [d["name"] for d in destinations])

# --- 랜덤 추천 버튼 ---
if st.sidebar.button("🎲 오늘의 랜덤 추천!"):
    selected = random.choice(destinations)["name"]
    st.sidebar.success(f"✨ 추천 여행지는 **{selected}** 입니다!")

# --- 선택된 여행지 정보 표시 ---
for place in destinations:
    if place["name"] == selected:
        col1, col2 = st.columns([1, 1.5])
        with col1:
            st.image(place["img"], use_column_width=True, caption=place["name"])
        with col2:
            st.subheader(f"📍 {place['name']}")
            st.markdown(place["description"], unsafe_allow_html=True)
        break

# --- Folium 지도 ---
m = folium.Map(location=[26.5, 30.5], zoom_start=5, tiles="CartoDB positron")

# 마커 추가
for d in destinations:
    folium.Marker(
        location=[d["lat"], d["lon"]],
        tooltip=d["name"],
        popup=folium.Popup(f"<b>{d['name']}</b><br>{d['description']}", max_width=250),
        icon=folium.Icon(color="orange" if d["name"] == selected else "blue")
    ).add_to(m)

st.markdown("### 🗺️ 이집트 여행지 지도 보기")
st_folium(m, width=800, height=500)

# --- 마무리 ---
st.divider()
st.markdown("💡 <i>고대의 신비가 살아 숨 쉬는 이집트, 어디부터 탐험하고 싶나요?</i>", unsafe_allow_html=True)

