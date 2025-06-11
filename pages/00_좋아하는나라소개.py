import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="내가 좋아하는 여행지", layout="centered")

st.title("🌍 내가 좋아하는 여행지 소개")

places = {
    "파리 (프랑스)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg",
        "description": "에펠탑, 루브르 박물관, 세느강이 아름다운 예술과 낭만의 도시 파리!",
        "coordinates": (48.8566, 2.3522),
        "video": "https://www.youtube.com/watch?v=8ZqDOk8U_9I"
    },
    "교토 (일본)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Kiyomizu-dera_in_Kyoto%2C_Japan.jpg",
        "description": "전통과 자연이 어우러진 아름다운 도시, 교토. 사찰과 벚꽃 명소가 많아요.",
        "coordinates": (35.0116, 135.7681),
        "video": "https://www.youtube.com/watch?v=cWqL9IytK2A"
    },
    "바르셀로나 (스페인)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Barcelona_collage.jpg",
        "description": "가우디의 도시, 바르셀로나! 사그라다 파밀리아 성당과 맛있는 음식이 매력적이에요.",
        "coordinates": (41.3851, 2.1734),
        "video": "https://www.youtube.com/watch?v=RkZkekS8NQU"
    }
}

selected_place = st.selectbox("🔍 여행지를 선택하세요:", list(places.keys()))
place = places[selected_place]

st.image(place["image"], use_column_width=True)
st.markdown(f"**{selected_place}**")
st.write(place["description"])

# 지도 출력
m = folium.Map(location=place["coordinates"], zoom_start=12)
folium.Marker(location=place["coordinates"], popup=selected_place).add_to(m)
st_folium(m, width=700)

# 유튜브 영상 출력
st.video(place["video"])
