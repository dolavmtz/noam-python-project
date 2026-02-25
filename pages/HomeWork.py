import streamlit as st
from Helper import *
import PIL.Image

st.page_link("main.py", label="🏠 חזרה לדף הבית")

st.set_page_config(
    page_title = "בוט שיעורי בית",
    page_icon = '🤓'

)

setRTL()

newPage("homework")

st.title("בוט שיעורי בית")

API_KEY = getAPIkey()

systemPrompt = """
    #תפקיד
    אתה בוט שיעורי בית
    
    #משימה
    המשימה שלך - לעזור לי בשיעורי בית
    תסביר ברור

    
    #מגבלות
    אם אתה לא יודע - תחפש בגוגל
   **אל תמציא תשובה**
    ענה כמו בן אדם - בצורה אנושית
    
    ** אם השתמשת בכלי (Tool) תכתוב את התוצאה **
    **אנחנו בשנת 2026**
    **יש לך אפשרות ב(tool) לבדוק את התאריך ושעה אם נדרש להשתמש**
"""


st.session_state.system_prompt = systemPrompt

Message("AI","היי איך אפשר לעזור לך")

for m in st.session_state.history:
    Message(m["role"],m["text"])

userinput = st.chat_input("השאלה שלך... ")

image_input = st.file_uploader( "העלאת תמונה", type=["jpg","png","jpeg"])


if userinput:
    image = None
    if image_input:
        image = PIL.Image.open(image_input)
        print(image)
    Message("User",userinput)
    with st.spinner("חושב..."):
        sendMessage(userinput, image)
