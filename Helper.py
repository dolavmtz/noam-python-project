from dotenv import load_dotenv
import os
import streamlit as st
from google import genai


all_models = ["gemini-2.5-flash-lite",
              "gemini-2.5-flash",
              "gemini-2.0-flash",
              "gemini-2.0-flash-lite",
              "gemini-3.0-flash"]

def create_chat():
    client = genai.Client(api_key=getAPIkey())

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
        self.role = role #מי שלח את ההודעה
        self.text = text #מה הוא שלח
        self.showMessage() #תציג את ההודעה

    def showMessage(self):
        message = st.chat_message(self.role)
        message.write(self.text)

