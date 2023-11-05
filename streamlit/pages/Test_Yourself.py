import streamlit as st

def choose_subject():
    st.header("Test yourself! 👨🏻‍🎓")

    # Initialize session state to keep track of the selected subject
    if 'selected_subject' not in st.session_state:
        st.session_state.selected_subject = None

    if st.button("Science"):
        st.session_state.selected_subject = 'Science'

    if st.button("English"):
        st.session_state.selected_subject = 'English'

    # Display the selected subject's page based on the button click
    if st.session_state.selected_subject == 'Science':
        science()
    elif st.session_state.selected_subject == 'English':
        english()

# Create a function to display and evaluate questions
def mcq_test(s):
    # Define your questions and answer choices
    if s == "s":
        questions = [
        {
            'question': 'What is the chemical symbol for gold?',
            'choices': ['Go', 'Gl', 'Au', 'Ag'],
            'correct_choice': 'Au',
            'selected_choice': None,
        },
        {
            'question': 'Which gas is most abundant in Earth\'s atmosphere?',
            'choices': ['Oxygen', 'Carbon dioxide', 'Nitrogen', 'Argon'],
            'correct_choice': 'Nitrogen',
            'selected_choice': None,
        },
        {
            'question': 'What is the smallest unit of matter?',
            'choices': ['Molecule', 'Element', 'Atom', 'Compound'],
            'correct_choice': 'Atom',
            'selected_choice': None,
        },
        {
            'question': 'Which of the following is a renewable energy source?',
            'choices': ['Natural Gas', 'Coal', 'Solar Energy', 'Oil'],
            'correct_choice': 'Solar Energy',
            'selected_choice': None,
        }
    ]
    else:
        questions = [
        {
            'question': 'Who is the author of the play "Romeo and Juliet"?',
            'choices': ['William Shakespeare', 'Charles Dickens', 'Mark Twain', 'Jane Austen'],
            'correct_choice': 'William Shakespeare',
            'selected_choice': None,
        },
        {
            'question': 'What is the meaning of the literary term "metaphor"?',
            'choices': ['A comparison using "like" or "as"', 'Directly stating the characteristics of something', 'Symbolic representation of something', 'A type of poem'],
            'correct_choice': 'Symbolic representation of something',
            'selected_choice': None,
        },
        {
            'question': 'Identify the figure of speech: "The world is a stage."',
            'choices': ['Metaphor', 'Simile', 'Personification', 'Hyperbole'],
            'correct_choice': 'Metaphor',
            'selected_choice': None,
        },
        {
            'question': 'Who wrote the novel "To Kill a Mockingbird"?',
            'choices': ['Harper Lee', 'J.K. Rowling', 'Ernest Hemingway', 'F. Scott Fitzgerald'],
            'correct_choice': 'Harper Lee',
            'selected_choice': None,
        }
    ]
    

    score = 0
    for i, question in enumerate(questions):
        st.write(f"**Question {i+1}:** {question['question']}")
        question_id = f"question_{i}"

        if question['selected_choice'] is None:
            user_choice = st.radio("Choose an answer:", question['choices'], key=question_id, index=None)
            if user_choice is not None:
                question['selected_choice'] = user_choice

        if question['selected_choice'] is not None:
            if question['selected_choice'] == question['correct_choice']:
                # st.success("Correct!")
                score += 1
            # else:
                # st.error("Incorrect. The correct answer is: " + question['correct_choice'])
        else:
            st.write("Please select an answer to reveal the result for this question.")

    if st.button("Submit"):
        st.write(f"Your score: {score}/{len(questions)}")

        if score>2:
            st.success("Good job! You're getting the hang of this!")
        else:
            st.error("Not bad, but let's practice more!")

    
def science():

    st.subheader("Answer the following questions:")
    mcq_test("s")

def english():

    st.subheader("Answer the following questions:")
    mcq_test("e")

if __name__ == '__main__':
    choose_subject()
