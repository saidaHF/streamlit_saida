import streamlit as st
import skills
import prueba
import aboutme

initial_content = st.empty() 

def showHome():
    initial_content.write("¡Bienvenido! Este es el contenido inicial que desaparecerá al hacer clic en un menú.")

def hideHome():
    initial_content.empty()
    
showHome()

if st.sidebar.button('Home'):
    showHome()

if st.sidebar.button('About me'):
    hideHome()
    aboutme.showAboutMe()

if st.sidebar.button('My Skills'):
    hideHome()
    skills.showSkills()

if st.sidebar.button('Websites'):
    hideHome()
    prueba.showPrueba()

