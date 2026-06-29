import streamlit as st
from Helper import *
import PIL.Image

st.page_link("main.py", label="🏠 חזרה לדף הבית")

st.set_page_config(
    page_title="סוכן קוד",
    page_icon='🤓'

)

def ask_question(question:str,options:list[str]) ->str:
    """
    כלי לשאילת שאלה כדי להבהיר מצב כלשהו
    כל פעם שולח שאלה אחת + 2-4 אפשרויות שאתה רוצה לשאול את המשתמש
    :param question: השאלה שאתה שואל
    :param options: אפשרויות מתאימות 2-4
    :return: סטטוס
    """
    st.session_state.question = question
    st.session_state.options = options
    st.session_state.status = "wait for answer"
    return "השאלה נשלחה"


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
    
    #יכולות
    אם אתה רוצה לשאול שאלות - תפעיל את הכלי ask_question עם שאלה ובין 2-4 אפשרויות
    כתוב ל י "כמה שאלות כדי להמשיך:"
"""

tools.append(ask_question)
st.session_state.system_prompt = systemPrompt


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
                    print(options[i] + "נבחר")


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
