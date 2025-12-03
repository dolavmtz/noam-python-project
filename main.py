import streamlit as st

st.set_page_config(
    page_title="הפרויקטים של נועם",
    page_icon="👑",
    layout="wide"
)

# --- עיצוב (ימין + העלמת סטרימליט) ---
st.markdown("""
<style>
.block-container {
    direction: rtl;
    text-align: right;
}
header, footer {
    visibility: hidden;
}
.nav-box {
    background: #eef1ff;
    padding: 15px;
    border-radius: 14px;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)


# --- תפריט ניווט אמיתי עם page_link ---
with st.container():
    st.markdown('<div class="nav-box">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.page_link("main.py", label="🏠 דף הבית")

    with col2:
        st.page_link("Pages/Alias.py", label="🎮 משחק אליאס")


    st.markdown('</div>', unsafe_allow_html=True)


# --- תוכן הדף ---
st.title("ברוכים הבאים לאתר הפרויקטים של נועם ✨")

st.subheader("מי אנחנו?")
st.write("""
אנחנו נועם והצוות, מפתחים פרויקטים מגניבים 👨‍💻👩‍💻  
באתר הזה תוכלו למצוא אפליקציות, משחקים וכלי קוד שבנינו.
""")

st.subheader("הפרויקטים שלנו")
st.write("בחרו אחד מהפרויקטים בתפריט למעלה 👆")
