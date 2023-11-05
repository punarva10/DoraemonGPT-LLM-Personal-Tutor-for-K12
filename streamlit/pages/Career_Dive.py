import streamlit as st

st.set_page_config(layout="wide")

# Define a list of career options
career_choices = [
    "Software Developer", "Data Scientist", "Graphic Designer", "Doctor",
    "Engineer", "Entrepreneur", "Teacher", "Chef", "Athlete",
    "Artist", "Architect", "Musician", "Writer", "Police Officer",
    "Astronaut", "Lawyer", "Psychologist", "Pilot", "Environmental Scientist",
    "Biomedical Engineer", "Dentist", "Pharmacist", "Veterinarian",
    "Fashion Designer", "Marketing Manager", "Physical Therapist", "Biologist",
    "Chemist", "Geologist", "Agricultural Scientist", "Social Worker",
    "Event Planner", "Plumber", "Mechanic",
    "Electrician", "Flight Attendant", "Meteorologist", "Librarian",
    "Zoologist", "Paramedic", "Translator", "Fitness Trainer",
    "Marine Biologist", "Sculptor", "Cinematographer", "Agricultural Engineer",
    "Fashion Model", "Makeup Artist", "Sales Representative",
    "Crime Scene Investigator", "Firefighter", "Judge", "Museum Curator",
    "Travel Blogger", "Podcaster", "Content Creator",
    "Financial Analyst", "Environmental Lawyer", "Interior Designer", "App Developer",
    "Gaming Designer", "Ethical Hacker", "Personal Trainer", "Chef de Cuisine",
    "Sports Coach", "Digital Marketer", "Data Analyst", "Robotics Engineer",
]

# Set the title and a brief introduction

st.title("Career Discovery for Teens")
st.write("Welcome to the career discovery page! Choose a career to learn more about it.")
st.subheader("No matter what career you choose, remember that hard work and dedication can lead you to success!")

# Create a grid layout for buttons
cols = st.columns(6)  # Create 3 columns for the buttons

# Create buttons for each career option in a grid layout
for i, career in enumerate(career_choices):
    try:
        col = cols[i % 6]  # Distribute the buttons across the 3 columns
        if col.button(career):
            st.session_state.selected_career = career
    except:
        st.write(career)

