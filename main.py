import streamlit as st
st.title('윤효린의 첫번째 앱!')
st.subheader('오늘 저녁 뭐 먹지')
st.write('하하하')
st.write('https://naver.com')
st.link_button('네이버 바로 가기','https://naver.com')

name=st.text_input('이름을 입력해주세요')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요')
    st.balloons()
    st.image('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTBfMzkg%2FMDAxNzI4NTU1NjY5MDM1._1P_R36fsDFy_FSK9EUsMX0sx6ieaUcwRaSpGTHJWHIg.XSZlMjzPI5QcGEFvYO0zkHEua83O6mhNpfFyzWsGuhMg.PNG%2F%25C5%25E4%25B3%25A2%25B6%25EC%25BF%25CD%25C0%25DF%25B8%25C2%25B4%25C2%25B6%25EC_%25B1%25C3%25C7%25D5_%25BB%25F3%25B1%25D8.png&type=sc960_832')

st.success('성공!')
st.warning('경고')
st.error('오류')

