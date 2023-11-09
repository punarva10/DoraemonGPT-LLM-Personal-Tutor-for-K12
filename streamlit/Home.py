import streamlit as st

def main():
    st.header("Welcome to Doraemon's Study Zone!")
    image_path = "pic.png"
    width = 500  # Replace with your desired width

    # Display the image with the specified size
    st.image(image_path, width=width,caption="Study together with Doraemon!")

    st.subheader("📚🤖 Come study with me! I'm Doraemon, your study buddy. Explore the world of learning with fun and excitement. Let's make studying an adventure! 🚀✨")

if __name__ == '__main__':
    main()