import os

from dotenv import load_dotenv
from google import genai
import streamlit as st
from Helper import *


setRTL()

newPage("Alias")


st.set_page_config(
    page_title = "משחק אליאס",
    page_icon = '🤖'

)


st.page_link("main.py", label="🏠 חזרה לדף הבית")



st.title("משחק אליאס")


# load_dotenv()
# API_KEY = os.getenv("API_KEY")

API_KEY = getAPIkey()


def start():
    st.session_state.end = False
    st.session_state.gemini = genai.Client(api_key=API_KEY)
    st.session_state.history = []
    message = send(prompt)
    # st.text(message)
    # st.session_state.history.append()
    # ai_text =st.chat_message("ai")
    # ai_text.write(message)


prompt = """
        ### הקשר
        אנחנו במשחק "אליאס" - שזה משחק ניחושים
        עליך להגריל מילה ואני צריך לנחש מה המילה שהגרלת
        אתה צריך לתת לי רמזים 

        ### חוקים
        אסור שהמילה או השורש שלה יופיעו
        תן 1 רמזים ולאט לאט תיהיה יותר ספציפי
        אל תגלה את המילה אלה עם כן אני אבקש
        אסור לך לומר לי את המילה במהלך המשחק
        
        ### סיום משחק
        לאחר 3 ניסיונות או הצלחה כתוב את המילה שהגרלת
        כתוב בסיום END
"""

print("מתחיל...")

all_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash-lite"]


def send(prompt):
    st.session_state.loadin = True
    st.session_state.history.append({
        "sender": "user",
        "text": prompt
    })
    context = "n\ זו השיחה המלאה:"
    for line in st.session_state.history:
        context += f"{line['sender']}: {line['text']}\n"
    with st.spinner("חושב...", show_time=True):
        for model in all_models:
            print(model)
            chat = st.session_state.gemini.chats.create(model=model)
            try:
                message = chat.send_message(context)
                st.session_state.history.append({
                    "sender": "ai",
                    "text": message.text
                })
                st.session_state.loadin = False
                return message.text
            except:
                print("לא הצליח - אנסה את המדל הבא")


if "gemini" not in st.session_state:
    start()

if 'history' in st.session_state and len(st.session_state.history) > 0:
    for line in st.session_state.history[1:]:
        chat = st.chat_message(line["sender"])
        chat.write(line["text"])

if 'end' in st.session_state and st.session_state.end:
    st.balloons()
    st.success("המשחק הסתיים")




# chat = gemini.chats.create(model="gemini-2.5-flash-lite") #יוצרים צאט חדש

# message = send(prompt)
# st.text(message)

else:
    user = st.chat_input("ניחוש")
    if user:
        user_text = st.chat_message("user")
        user_text.write(user)

        ai = send("הניחוש: " + user)
        ai_text = st.chat_message("ai")
        ai_text.write(ai)

        if 'END' in ai:
            st.session_state.end = True
            st.rerun()

#  st.rerun()


# while True:
# user = input("הניחוש שלך >>>")
# message = chat.send_message(user)
# print(message.text)
# if "END" in message.text:
#     break

# to = input("למי לכתוב ברכה? >>")
# content = input("למתי לכתוב הברכה? >>")
# addons = input("מידע חשוב נוסף כדי לכתוב את הברכה >>")
# prompt = f"""אתה מומחה לכתיבת ברכות
#             כתוב ברכה ל{to}
#             לכבוד{content}
#             שים לב ש{addons}
#             עד 3 שורות, תוסיף אימוג'ים
# """
#
#
# gemini = genai.Client(api_key=API_KEY)
# ai = gemini.chats.create(model="gemini-2.5-flash")
# message = ai.send_message(p)
# print(message.text)