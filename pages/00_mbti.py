import streamlit as st

# 제목 🎬✨
st.set_page_config(page_title="🌟MBTI 배우 추천🌟", page_icon="🎭", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🌈 MBTI 배우 추천 🌈</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>✨ 너의 MBTI에 맞는 최고의 배우를 찾아보자! 🎉🎬</p>", unsafe_allow_html=True)

# MBTI 선택
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("💡 너의 MBTI를 선택해줘! 💡", mbti_list)

# MBTI별 배우 추천 데이터
mbti_actors = {
    "ISTJ": "🧑‍💼 이병헌 🎩",
    "ISFJ": "👩‍🎤 박보영 🌸",
    "INFJ": "🧑‍🎨 박서준 🎨",
    "INTJ": "👨‍💻 정우성 💎",
    "ISTP": "🏍️ 유아인 🔥",
    "ISFP": "🎹 아이유 🎵",
    "INFP": "🌿 박보검 🌙",
    "INTP": "🔬 류준열 🧪",
    "ESTP": "⚡ 김수현 🏆",
    "ESFP": "🎉 전지현 💃",
    "ENFP": "🌈 송강 🌟",
    "ENTP": "💡 공유 🚀",
    "ESTJ": "🛡️ 하정우 🏹",
    "ESFJ": "🌸 손예진 💖",
    "ENFJ": "🔥 현빈 🎬",
    "ENTJ": "💎 조인성 🏰"
}

# 추천 결과 출력
st.markdown(f"### 🌟 너의 MBTI는 {selected_mbti} 🌟")
st.markdown(f"🎬 추천 배우: **{mbti_actors[selected_mbti]}** 🎬")
st.balloons()  # 풍선 팡팡 🎈🎈

# 추가 설명 (화려하게)
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #FF69B4;
    color: white;
    font-size: 20px;
    border-radius: 15px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

if st.button("💖 배우 더 보기 💖"):
    st.markdown("✨ 다음 배우도 궁금하다면 이 버튼을 눌러보세요! 🌟")
