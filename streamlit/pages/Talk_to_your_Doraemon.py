import streamlit as st
from langchain.llms import GooglePalm

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

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