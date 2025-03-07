import streamlit as st
import skills
import websites
import aboutme
import os

from pathlib import Path

current_dir = os.path.dirname(__file__)
css_file = os.path.join(current_dir, 'assets', 'styles.css')

with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

initial_content = st.empty() 

def showHome():
    initial_content.write("Welcome! We're under construction, sorry")

    image_path = Path("main/resources/funny_image.gif")
    st.image(str(image_path), clamp=True)

def hideHome():
    initial_content.empty()
    
showHome()

if st.sidebar.button('Home 🏠'):
    showHome()

if st.sidebar.button('About me 🧙🏻‍♀️'):
    hideHome()
    aboutme.showAboutMe()

if st.sidebar.button('My Skills 🔨'):
    hideHome()
    skills.showSkills()

if st.sidebar.button('Websites'):
    hideHome()
    websites.showWebSites()
