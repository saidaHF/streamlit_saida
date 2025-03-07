import streamlit as st

from pathlib import Path


def showAboutMe():
    st.title("Welcome to my profile!!!")
    # Get the absolute path to the image dynamically
    image_path = Path("main/resources/saida_dibujo.png")

    # Create two columns
    col1, col2 = st.columns([5, 10])

    # Add image to the first column
    with col1:
        st.image(str(image_path), caption="Saida", clamp=True)

    # Add text to the second column
    with col2:
        st.markdown("""
        Hi, I'm Saida! 🧙🏻‍♀️

        I’m a passionate full-stack developer with strong experience in **Python** and **Vue/Angular**. 
        I specialize in backend development, but I’m also keen on learning and working with **Big Data** and **Artificial Intelligence**. 
        I have a solid foundation in **Deep Learning**, which fuels my enthusiasm for working on projects related to cutting-edge technology like AI and machine learning.

        **What drives me?**
        - **Python** is my language of choice — it's my go-to tool for both **backend development** and exploring data.
        - I enjoy solving complex problems, optimizing systems, and finding elegant solutions.

        When I’m not coding, you can find me indulging in my other passions:
        - 🌌 **Physics** and **Astronomy** — I love exploring the mysteries of the universe.
        - 🐾 **Animals** — I have a dog (Tala 🐶) and two cats (Galileo 🐱 and Saphira 🐱).
        - 🍳 **Cooking** — I’m always experimenting with new recipes, so feel free to ask me for a tasty dish recommendation!
        - 🎨 **Drawing** — I absolutely love to draw in my free time. Whether it’s digital or traditional art, it’s my way of expressing creativity and relaxing.

        I’m excited about the possibility of applying my skills to work on projects that make an impact in **Big Data** and **AI**.
        """)
