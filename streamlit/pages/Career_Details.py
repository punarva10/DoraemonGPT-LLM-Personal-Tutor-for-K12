import streamlit as st
from langchain.llms import GooglePalm
from streamlit_extras.switch_page_button import switch_page

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
    careful_prompt = 'I am 13 years old. Please give answers according to the topic that is {st.session_state.selected_career}. Under no circumstance should you give me inappropriate responses. If you think the answer is not suitable for a 13 year old, reply with "I am not under circumstances to answer this question. Please ask a different one"'
    try:
        st.write(llm(careful_prompt+ user_question))
    except:
        st.write('I am not under circumstances to answer this question. Please ask a different one')

def main():
    if "selected_career" not in st.session_state:
        switch_page('Career Dive')

    st.set_page_config(page_title=f'{st.session_state.selected_career}')
    st.header(f'Ask anything about {st.session_state.selected_career}')

    st.write(css, unsafe_allow_html = True)

    handle_userinput(f'Explain the field of {st.session_state.selected_career} as though you are explaining it to a 14 year old in not more than 300 words.')

    user_question = st.text_input(f"What else do you want to know about {st.session_state.selected_career}?")
    if user_question:
        handle_userinput(user_question)

if __name__ == "__main__":
    main()