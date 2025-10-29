import streamlit as st

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="💋 한소희 감성 꾸미기 게임 💄",
    page_icon="💄",
    layout="wide",
)

# -----------------------------
# CSS - 섹시하고 고급스러운 네온 핑크 감성
# -----------------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top left, #1b0026, #000000 80%);
    background-attachment: fixed;
    color: white;
}
@keyframes neonPulse {
  0%, 100% { text-shadow: 0 0 15px #ff4d88, 0 0 25px #ff4d88, 0 0 40px #ff1e56; }
  50% { text-shadow: 0 0 5px #ff1e56, 0 0 15px #ff4d88, 0 0 25px #ff4d88; }
}
.title {
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#ff4d88;
    animation: neonPulse 2s infinite;
}
.subtitle {
    text-align:center;
    font-size:20px;
    color:#ffb6c1;
    margin-bottom:40px;
}
.card {
    background: rgba(40, 0, 30, 0.6);
    border-radius: 25px;
    padding: 25px;
    text-align:center;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 40px rgba(255,0,100,0.6);
    transition: all 0.3s ease;
}
.card:hover {
    transform: scale(1.04);
    box-shadow: 0 0 60px rgba(255,0,150,1);
}
.card img {
    border-radius: 20px;
    width:100%;
    box-shadow: 0 0 30px rgba(255,0,90,0.8);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown('<h1 class="title">💄 한소희 감성 꾸미기 💋</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ 당신의 스타일 감각으로 “한소희 감성”을 완성해보세요 ✨</p>', unsafe_allow_html=True)

# -----------------------------
# 옵션 선택
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    outfit = st.selectbox("👗 의상 스타일", ["시크 블랙 드레스", "로맨틱 핑크 셋업", "실버 글리터 수트", "레드 카펫 드레스"])
with col2:
    vibe = st.selectbox("🔥 무드", ["섹시 카리스마", "청순 도도함", "우아한 시크", "치명적인 눈빛"])
with col3:
    bg = st.selectbox("🌃 배경 무드", ["네온 시티", "무대 조명", "로즈 라운지", "패션쇼 런웨이"])
with col4:
    acc = st.selectbox("💎 포인트 액세서리", ["초커", "골드 이어링", "루비 반지", "실버 체인"])

# -----------------------------
# 이미지 매핑 (가상 인물 이미지 예시)
# -----------------------------
image_map = {
    ("시크 블랙 드레스", "네온 시티"): "https://cdn.pixabay.com/photo/2021/10/07/07/59/woman-6688453_1280.jpg",
    ("로맨틱 핑크 셋업", "로즈 라운지"): "https://cdn.pixabay.com/photo/2020/11/17/20/22/woman-5752041_1280.jpg",
    ("실버 글리터 수트", "무대 조명"): "https://cdn.pixabay.com/photo/2021/12/20/21/56/woman-6884558_1280.jpg",
    ("레드 카펫 드레스", "패션쇼 런웨이"): "https://cdn.pixabay.com/photo/2021/07/21/05/46/woman-6483479_1280.jpg",
}

img_url = image_map.get((outfit, bg), "https://cdn.pixabay.com/photo/2021/08/05/23/52/fashion-6523395_1280.jpg")

# -----------------------------
# 결과 카드
# -----------------------------
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:50px;">
    <div class="card" style="width:430px;">
        <img src="{img_url}">
        <h3>👗 의상: {outfit}</h3>
        <p>🔥 무드: {vibe}</p>
        <p>🌃 배경: {bg}</p>
        <p>💎 액세서리: {acc}</p>
        <p style="font-size:22px; color:#ffb6c1;">💋 완성된 한소희 감성 스타일 💋</p>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 효과
# -----------------------------
st.markdown("<p style='text-align:center; font-size:35px;'>💋🔥👠💎🌃✨</p>", unsafe_allow_html=True)
st.snow()
