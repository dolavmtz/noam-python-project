import streamlit as st
from Helper import *

setRTL()

st.set_page_config(
    page_title="הפרויקטים של נועם",
    page_icon="👑",
    layout="wide"
)

# --- עיצוב נקי, צבעוני, ללא רווחים מיותרים ---
st.markdown("""
<style>
.block-container {
    direction: rtl;
    text-align: right;
    max-width: 900px;
    padding-top: 20px;
}
header, footer { visibility: hidden; }

.nav-box {
    background: linear-gradient(135deg, #dfe7ff, #f2f4ff);
    padding: 0px 0px;
    border-radius: 0px;
    margin-bottom: 0px;
    border: 1px solid #cbd5ff;
    display: inline-block;
}

.title-box {
    background: white;
    padding: 0px;
    border-radius: 20px;
    border: 1px solid #e6e6e6;
    box-shadow: 0 0px 0px rgba(0,0,0,0.00);
}

h1 { color: #2a2d46 !important; }
h2 { color: #3c3f60 !important; }
p, .stMarkdown { color: #4a4c63 !important; }
</style>
""", unsafe_allow_html=True)

# --- ניווט נקי וללא בלוקים ריקים ---
st.markdown('<div class="nav-box">', unsafe_allow_html=True)
st.page_link("Pages/Alias.py", label="🎮 משחק אליאס")
st.markdown('</div>', unsafe_allow_html=True)

st.page_link("Pages/Homework.py", label="📚 מעבר לבוט שיעורי בית")


# --- תוכן הדף ---
st.markdown('<div class="title-box">', unsafe_allow_html=True)

st.title("ברוכים הבאים לאתר הפרויקטים של נועם✨")

st.write("""
בניתי לכם כל מיני משחקים וכלים שתוכלו להשתמש בהם תהנו!! 
""")

st.subheader("התחילו מכאן:")
st.write("בחרו פרויקט מהתפריט למעלה 👆")

st.markdown('</div>', unsafe_allow_html=True)