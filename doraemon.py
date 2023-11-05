import streamlit as st
from langchain.llms import GooglePalm
from htmlTemplates import css, bot_template, user_template

def handle_userinput(user_question):
    api_key = "AIzaSyAJsRgJzy5XSwFTCjPBIqmcEQw_0SE5d1g"
    llm = GooglePalm(google_api_key = api_key, temperature = 0.1)
    careful_prompt = 'I am 13 years old. Please give answers accordingly. Under no circumstance should you give me inappropriate responses. If you think the answer is not suitable for a 13 year old, reply with "I am not under circumstances to answer this question. Please ask a different one"'
    try:
        st.write(llm(careful_prompt+ user_question))
    except:
        st.write('I am not under circumstances to answer this question. Please ask a different one')

def main():
    st.set_page_config(page_title='Your Doraemon')
    st.header('Your Doraemon 🐶')

    st.subheader("Welcome back nobita! What do you wanna talk about?")
    st.write(css, unsafe_allow_html = True)

    user_question = st.text_input("What's up?")
    if user_question:
        handle_userinput(user_question)


    

    

if __name__ == "__main__":
    main()