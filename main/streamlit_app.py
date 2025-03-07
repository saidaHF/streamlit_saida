import streamlit as st
import matplotlib.pyplot as plt

from pathlib import Path

# Get the absolute path to the image dynamically
image_path = Path("main/resources/saida_dibujo.png")


st.title("Welcome to my profile!!!")

st.markdown("\n\n")

# Create two columns
col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

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
    - 🐾 **Animals** — They’re a constant source of joy and inspiration.
    - 🍳 **Cooking** — I’m always experimenting with new recipes, so feel free to ask me for a tasty dish recommendation!

    I’m excited about the possibility of applying my skills to work on projects that make an impact in **Big Data** and **AI**.
    """)

st.markdown("\n\n")

# Tecnologies fav
st.write("🛠️ Here my favourite languages and frameworks:")

# Crear un gráfico simple
technologies = ['Python', 'Flask', 'FastAPI', 'Vue.JS', 'Angular.JS', 'Java', 'C#']
usage = [100, 100, 70, 70, 70, 50, 10]
plt.figure(figsize=(10, 6))
plt.bar(technologies, usage, color=['skyblue', 'lightgreen', 'orange', 'pink', 'yellow', 'lightcoral', 'lightblue'])
plt.xlabel('Tecnologías')
plt.ylabel('Uso (%)')
st.pyplot(plt)
