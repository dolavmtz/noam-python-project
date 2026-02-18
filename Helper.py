import time

from dotenv import load_dotenv
import os
import streamlit as st
from google import genai
from google.genai import types

from ddgs import DDGS


def web_search(query :str) ->str:
    print("searching: " + query)
    """
    פונקציה שמקבלת ערכים לחיפוש ומחזירה תוצאות מובילות
    הפונקציה תקבל טקסט לחיפוש(עדיף שיהיה כתוב באנגלית)
    ותחזיר את התוצאות
    """
    with st.status("searching: " + query):

        with DDGS() as d:
            results = d.text(query,max_results=3)
            return results

st.session_state.page = ""
def newPage(pagename):
    if st.session_state.page != pagename:
        print("דף חדש")
        st.session_state.page = pagename
        st.session_state.history = []

all_models = ["gemini-2.5-flash-lite",
              "gemini-2.5-flash",
              "gemini-3.0-flash",
              "gemini-2.0-flash",
              "gemini-2.0-flash-lite"]

def currentTime():
    print("use tool")
    """ 
    כלי שיודע מה הזמן עכשיו  ומחזיר טקסט של הזמן הנוכחי
    """
    return time.ctime()

def create_chat(model,instruction,history=[]):
    if "client" not in st.session_state:
        st.session_state.client = genai.Client(api_key=getAPIkey())
    if instruction == "":
        if "system_prompt" in st.session_state:
            instruction = st.session_state.system_prompt


    st.session_state.chat = st.session_state.client.chats.create(
            model = model,
            history = history,
            config = types.GenerateContentConfig(
                system_instruction =  instruction,
                tools = [currentTime, web_search],
                automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
            )
        )
    print(st.session_state.chat)

st.session_state.modelIndex = 0

maxTrys = 5
currentTrys = 0

if "history" not in st.session_state:
    st.session_state.history = []



def sendMessage(prompt):
    st.session_state.history.append(
        {
            "role": "user",
            "text": prompt
        }
    )



    if "chat" not in st.session_state:
        create_chat(all_models[0],"")


    global currentTrys
    print(all_models[st.session_state.modelIndex])
    #st.caption(all_models[st.session_state.modelIndex])
    try:
        answer = st.session_state.chat.send_message(prompt)
        st.session_state.history.append(
            {
                "role": "model",
                "text": answer.text
            }
        )
        Message("ai",answer.text)
        currentTrys = 0
    except Exception as e:
        error = str(e)
        print(e)
        currentTrys +=1
        if currentTrys == maxTrys:
            st.error("תקלה-כל המודלים לא עובדים היום נסו שנית בפעם אחרת")
            return
        if "overloaded" in error.lower():
            newChat(prompt)
        if "429" in error:
            with st.spinner("יש יותר מידי קריאות - מחכים דקה...", show_time=True):
                time.sleep(60)
                newChat(prompt)
        if "503" in error:
            newChat(prompt)
def newChat(prompt):
    st.session_state.modelIndex += 1
    if st.session_state.modelIndex == len(all_models):
        st.session_state.modelIndex = 0
    newmodel = all_models[st.session_state.modelIndex]
    st.info(f"trying{newmodel}")
    create_chat(newmodel, "")
    sendMessage(prompt)




#פונקציה שטוענת את הAPI KEY  ומחזירה אותו
def getAPIkey():
    load_dotenv()
    API_KEY = os.getenv("API_KEY") or st.secrets["API_KEY"]
    return API_KEY

def setRTL():        #RTL  right to the left
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

#אובייקט "שולח" - מי שלח, מה ההודעה, אייקון להודעה
class Message:
    def __init__(self,role,text): #פונקציית הבניה  - self  - מי שיצרתי
        if role.lower() == "model":
            role = "ai"
        print(role,text)
        self.role = role #מי שלח את ההודעה
        self.text = text #מה הוא שלח
        self.showMessage() #תציג את ההודעה

    def showMessage(self):
        message = st.chat_message(self.role)
        message.write(self.text)

