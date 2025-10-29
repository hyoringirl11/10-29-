import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="💋 한소희 꾸미기 : 섹시 에디션 💄",
    page_icon="🔥",
    layout="wide",
)

# -----------------------------
# CSS : 섹시 네온 블랙 테마
# -----------------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top left, #3a0ca3, #000000 70%);
    color: white;
}
@keyframes neonGlow {
  0%, 100% {
    text-shadow: 0 0 10px #ff1e56, 0 0 20px #ff1e56, 0 0 40px #ff1e56;
  }
  50% {
    text-shadow: 0 0 5px #ff005c, 0 0 15px #ff005c, 0 0 30px #ff005c;
  }
}
.title {
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#ff1e56;
    animation: neonGlow 2s infinite;
}
.subtitle {
    text-align:center;
    font-size:22px;
    color:#ff99cc;
}
.card {
    background: rgba(40, 0, 30, 0.7);
    border-radius: 25px;
    padding: 25px;
    text-align:center;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 30px rgba(255,0,80,0.6);
    transition: 0.4s;
    color:white;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 60px rgba(255,0,100,1);
}
.card img {
    border-radius: 20px;
    width:100%;
    box-shadow: 0 0 40px rgba(255,0,80,0.8);
}
.selectbox label {
    color:#ff9ecd !important;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown('<h1 class="title">💄 한소희 꾸미기 : 섹시 에디션 💋</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🔥 당신의 취향으로 가장 섹시한 한소희를 완성해보세요 🔥</p>', unsafe_allow_html=True)

# -----------------------------
# 옵션 선택
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    style = st.selectbox("👠 의상 스타일", ["시크 블랙 드레스", "레드 슬립", "글리터 점프수트", "크롭 셋업"])
with col2:
    bg = st.selectbox("🌃 배경 무드", ["클럽 조명", "레드 카펫", "스모크 무대", "럭셔리 바"])
with col3:
    acc = st.selectbox("💎 액세서리", ["초커", "골드 이어링", "루비 반지", "실버 체인"])
with col4:
    vibe = st.selectbox("🔥 분위기", ["도도한 매력", "섹시 카리스마", "치명적인 눈빛", "묘한 미소"])

# -----------------------------
# 결과 매핑 (이미지 예시)
# -----------------------------
image_map = {
    ("시크 블랙 드레스", "클럽 조명"): "https://upload.wikimedia.org/wikipedia/commons/4/44/Han_So-hee_at_2023_Baeksang_Arts_Awards.jpg",
    ("레드 슬립", "레드 카펫"): "https://upload.wikimedia.org/wikipedia/commons/b/b5/Han_So-hee_in_2022.jpg",
    ("글리터 점프수트", "스모크 무대"): "https://upload.wikimedia.org/wikipedia/commons/6/6f/Han_So-hee_at_a_press_event_in_2023.jpg",
    ("크롭 셋업", "럭셔리 바"): "https://upload.wikimedia.org/wikipedia/commons/1/15/Han_So-hee_2022.jpg",
}

image_url = image_map.get((style, bg), "https://upload.wikimedia.org/wikipedia/commons/1/1a/Han_So-hee_2021.jpg")

# -----------------------------
# 결과 카드
# -----------------------------
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:40px;">
    <div class="card" style="width:450px;">
        <img src="{image_url}">
        <h3>👠 의상: {style}</h3>
        <p>🌃 배경: {bg}</p>
        <p>💎 액세서리: {acc}</p>
        <p>🔥 분위기: {vibe}</p>
        <p style="font-size:22px; color:#ff99cc;">💋 완성된 섹시 한소희 💋</p>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 애니메이션 효과
# -----------------------------
st.snow()
st.markdown("<p style='text-align:center; font-size:35px;'>💋🔥👠💎🌃✨</p>", unsafe_allow_html=True)
