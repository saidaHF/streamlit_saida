import streamlit as st
import matplotlib.pyplot as plt

def showSkills():
    # Tecnologies fav
    st.write("🛠️ Here my favourite languages and frameworks:")

    # Crear un gráfico simple
    technologies = ['Python', 'Flask', 'FastAPI', 'Vue.JS', 'Angular.JS', 'Java', 'C#']
    usage = [100, 100, 70, 70, 70, 50, 10]
    plt.figure(figsize=(10, 6))
    plt.bar(technologies, usage, color=['skyblue', 'lightgreen', 'orange', 'pink', 'yellow', 'lightcoral', 'lightblue'])
    plt.xlabel('Technologies')
    plt.ylabel('Use (%)')
    st.pyplot(plt)