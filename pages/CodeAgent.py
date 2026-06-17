import streamlit as st
from Helper import *
import PIL.Image

st.page_link("main.py", label="🏠 חזרה לדף הבית")

st.set_page_config(
    page_title="סוכן קוד",
    page_icon='🤓'

)

setRTL()

newPage("CodeAgent")

st.title("סוכן קוד")

API_KEY = getAPIkey()

systemPrompt = """
    אתה מומחה בתכנות. אתה יודע איך לתכנן ולפתח פרוייקטים משלב הרעיון ועד לקוד המלא
"""

st.session_state.system_prompt = systemPrompt


Message("AI", "היי, מה ניצור היום ביחד")


for m in st.session_state.history:
    Message(m["role"], m["text"])


userinput = st.chat_input("השאלה שלך... ")


image_input = st.file_uploader("העלאת תמונה", type=["jpg", "png", "jpeg"])


if userinput:
    image = None
 #   if image_input:
  #      image = PIL.Image.open(image_input)
   #     print(image)

    Message("User", userinput)
    with st.spinner("חושב..."):
        sendMessage(userinput)
