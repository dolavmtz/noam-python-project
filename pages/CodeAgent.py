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
    ##תפקיד
    אתה מומחה בתכנות. אתה יודע איך לתכנן ולפתח פרוייקטים משלב הרעיון ועד לקוד המלא
    
    ## איך אתה עושה את זה?
    1. אתה קודם כל מקבל רעיון, אם אין רעיון - תשאל שאלות כדי להציע רעיונות מתאימים
    2.תשאל שאלות כדי להבין יותר מה הכוונה
    3. תיצור תוכנית לפרויקט
    4. אחר כך - תחלק את הפיתוח לשלבים
    5. תפתח כל פעם שלב אחד
    6.תבדוק מה עשית ושזה טוב
    
    ##חוקים
    תענה בעברית, בצורה נעימה
    אם יש קוד עם סיכון - תשאל את המשתמש האם להשתמש - ותסביר מה השיקולים
    אל תתקדם אם  המשתמש לא אישר לך או עם חסר מידע
    הוסף הערות לקוד ותסביר תמיד קוד
    כתוב רק שאלה אחת בכל פעם והמתן לתשובה אל תעמיס על המשתמש
    שים לב לשאול שאלות רק דרך הtool
    
    #יכולות
    אם אתה רוצה לשאול שאלות - תפעיל את הכלי ask_question עם שאלה ובין 2-4 אפשרויות
    כתוב ל י "כמה שאלות כדי להמשיך:"
    אל תוסיף מידע נוסף מעבר לשאלות מהכלי
    תכתוב בכל שלב עד 3 שאלות וזהו
"""

steps = {
    "idea":"בחירת נושא",
    "plan" : "תוכנית",
    "development" : "שלבי פיתוח",
    "code" : "כתיבת קוד",
    "check" : "בדיקות"

}

if "completed_steps" not in st.session_state:
    st.session_state.completed_steps = []
if "current_steps" not in st.session_state:
    st.session_state.current_steps = "idea"


if ask_question not in tools:
    tools.append(ask_question)

st.session_state.system_prompt = systemPrompt

if "chosen_idea" not in st.session_state:
    st.session_state.idea = ""
if "plan" not in st.session_state:
    st.session_state.plan = ""
if "code_parts" not in st.session_state:
    st.session_state.code_parts = []

Message("AI", "היי, מה ניצור היום ביחד")


for m in st.session_state.history:
    Message(m["role"], m["text"])

if "status" not in st.session_state:
    st.session_state.status = "chat"

if st.session_state.status == "wait for answer":
    question = st.session_state.question
    options = st.session_state.options
    with st.chat_message("ai"):
        st.write(f"**{question}**")
        cols = st.columns(len(options))
        for i in range(len(cols)):
            with cols[i]:
                if st.button(options[i],key=f"o_{i}"):
                    Message("User",options[i])
                    st.session_state.status = "chat"
                    with st.spinner("חושב..."):
                        sendMessage(options[i])

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
