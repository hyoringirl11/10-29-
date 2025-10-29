import streamlit as st

# 페이지 설정
st.set_page_config(page_title="💥MBTI 배우 추천💥", page_icon="🎬", layout="wide")

# 헤더
st.markdown("""
<div style="text-align:center; background: linear-gradient(90deg, #ff7eb9, #ff65a3, #ff3f8b);
             padding: 30px; border-radius: 20px;">
    <h1 style="font-size:50px; color:white; font-weight:bold;">🌟 MBTI 배우 추천 🌟</h1>
    <p style="font-size:20px; color:white;">너의 MBTI에 맞는 최고의 배우를 만나보자! 🎭🔥</p>
</div>
""", unsafe_allow_html=True)

# MBTI 선택
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("💡 MBTI를 선택하세요! 💡", mbti_list)

# MBTI별 배우 추천 (사진 포함)
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

# 카드 형태 출력
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:30px;">
    <div style="background: linear-gradient(145deg, #ff9a9e, #fad0c4);
                border-radius: 25px; padding:20px; width:400px; text-align:center;
                box-shadow: 0 0 30px rgba(255,105,180,0.7); transition: transform 0.3s;">
        <img src="{actor['img']}" style="border-radius: 20px; width:100%; box-shadow: 0 0 20px rgba(0,0,0,0.2);" />
        <h2 style="color:#fff; font-weight:bold; margin-top:15px;">{actor['name']}</h2>
        <p style="color:#fff; font-size:16px;">✨ 너의 MBTI와 찰떡인 배우! 🌟</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 풍선과 반짝이 효과
st.balloons()
st.markdown("🎉✨🎬🌈💖💎🔥🕶️🌸💃🎨🎵⚡🌙🚀🏹🛡️", unsafe_allow_html=True)
