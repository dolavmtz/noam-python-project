import streamlit as st
from Helper import *

st.page_link("main.py", label="🏠 חזרה לדף הבית")

st.set_page_config(
    page_title = "בוט שיעורי בית",
    page_icon = '🤓'

)

setRTL()

st.title("בוט שיעורי בית")

API_KEY = getAPIkey()

systemPrompt = """
    ##תפקיד
    אתה עוזר בשיעורי בית
    
    ##משימה
    אתה צריך לוודא שהמידע תקין ונכון ותספק לי רק ממקורות אמינים לא מקורות כמו וויקיפדיה שכל אחד יכול לערוך
    נסה לכוון אותי לתשובה הנכונה
    תסביר מה התוכן
    
    
    ##מגבלות
    אם אתה לא יודע - תאמר "אני לא יודע" ואל תמציא 
    אם לא הבנת את השאלה - תגיד "לא הבנתי"
    **תנסח כמו אדם**
    **לעולם אל תשתמש בוויקפדיה המכלול או כל מקור שנחשב לא אמין ומדויק**
    

"""
st.session_state.system_prompt = systemPrompt

Message("AI","היי איך אפשר לעזור לך")

for m in st.session_state.history:
    Message(m["role"],m["text"])

userinput = st.chat_input("השאלה שלך... ")


if userinput:
    Message("User",userinput)
    sendMessage(userinput)
