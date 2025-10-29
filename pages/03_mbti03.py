import streamlit as st

# 페이지 설정
st.set_page_config(page_title="💥MBTI 배우 추천 레전드💥", page_icon="🎬", layout="wide")

# 배경 애니메이션 (CSS)
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 50% 50%, #ff9a9e, #fad0c4, #ffdde1, #fbc2eb);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
@keyframes gradientBG {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
.card {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    border-radius: 30px;
    padding: 25px;
    width: 350px;
    text-align:center;
    box-shadow: 0 0 40px rgba(255,105,180,0.8);
    transition: transform 0.4s, box-shadow 0.4s;
}
.card:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 0 60px rgba(255,20,147,1);
}
.card img {
    border-radius: 20px;
    width: 100%;
    box-shadow: 0 0 25px rgba(0,0,0,0.3);
}
h1.neon {
    color: #fff;
    font-size: 60px;
    text-shadow:
       0 0 5px #fff,
       0 0 10px #fff,
       0 0 20px #ff00de,
       0 0 30px #ff00de,
       0 0 40px #ff00de,
       0 0 55px #ff00de,
       0 0 75px #ff00de;
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<h1 class="neon" style="text-align:center;">💥 MBTI 배우 추천 💥</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:20px; color:#fff;">🌈 너의 MBTI와 찰떡인 배우를 만나보자! 🎬✨</p>', unsafe_allow_html=True)

# MBTI 선택
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
selected_mbti = st.selectbox("💡 MBTI를 선택하세요 💡", mbti_list)

# MBTI별 배우 추천
mbti_actors = {
    "ISTJ": {"name":"이병헌 🕶️", "img":"https://upload.wikimedia.org/wikipedia/commons/1/18/Lee_Byung-hun_Cannes_2017.jpg"},
    "ISFJ": {"name":"박보영 🌸", "img":"https://upload.wikimedia.org/wikipedia/commons/7/7b/Park_Bo-young_2019.png"},
    "INFJ": {"name":"박서준 🎨", "img":"https://upload.wikimedia.org/wikipedia/commons/2/27/Park_Seo-joon_at_the_2019.jpg"},
    "INTJ": {"name":"정우성 💎", "img":"https://upload.wikimedia.org/wikipedia/commons/5/5e/Jung_Woo-sung_at_Cannes.jpg"},
    "ISTP": {"name":"유아인 🔥", "img":"https://upload.wikimedia.org/wikipedia/commons/6/64/Yoo_Ahin_in_2016.jpg"},
    "ISFP": {"name":"아이유 🎵", "img":"https://upload.wikimedia.org/wikipedia/commons/9/9c/IU_at_the_2021.jpg"},
    "INFP": {"name":"박보검 🌙", "img":"https://upload.wikimedia.org/wikipedia/commons/4/44/Park_Bo-gum_at_Seoul.jpg"},
    "INTP": {"name":"류준열 🔬", "img":"https://upload.wikimedia.org/wikipedia/commons/2/2b/Ryu_Jun-yeol_at_Cannes_2018.jpg"},
    "ESTP": {"name":"김수현 ⚡", "img":"https://upload.wikimedia.org/wikipedia/commons/8/87/Kim_Soo-hyun_at_2017.jpg"},
    "ESFP": {"name":"전지현 💃", "img":"https://upload.wikimedia.org/wikipedia/commons/2/2f/Jun_Ji-hyun_2019.jpg"},
    "ENFP": {"name":"송강 🌈", "img":"https://upload.wikimedia.org/wikipedia/commons/1/18/Song_Kang.jpg"},
    "ENTP": {"name":"공유 💡", "img":"https://upload.wikimedia.org/wikipedia/commons/c/c0/Gong_Yoo_in_2019.jpg"},
    "ESTJ": {"name":"하정우 🛡️", "img":"https://upload.wikimedia.org/wikipedia/commons/7/7f/Ha_Jeong-woo_2017.jpg"},
    "ESFJ": {"name":"손예진 💖", "img":"https://upload.wikimedia.org/wikipedia/commons/9/9c/Son_Ye-jin_at_2019.jpg"},
    "ENFJ": {"name":"현빈 🔥", "img":"https://upload.wikimedia.org/wikipedia/commons/e/e6/Hyun_Bin_at_2019.jpg"},
    "ENTJ": {"name":"조인성 💎", "img":"https://upload.wikimedia.org/wikipedia/commons/6/63/Jo_In-sung_2019.jpg"}
}

actor = mbti_actors[selected_mbti]

# 카드 출력
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:40px;">
    <div class="card">
        <img src="{actor['img']}" />
        <h2 style="color:#fff; margin-top:15px;">{actor['name']}</h2>
        <p style="color:#fff; font-size:16px;">✨ 너의 MBTI와 찰떡인 배우! 🌟</p>
        <p style="font-size:20px;">🎬🔥💖🌈🕶️🌙🎨⚡💎</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 풍선 & 반짝이
st.balloons()
st.markdown("✨🎉💖💎🔥🌈🎬🕶️🌸💃🌙🎵⚡🚀🏹🛡️", unsafe_allow_html=True)
