import streamlit as st
from PIL import Image




def showWebSites():
    # Cargar imágenes
    github_image = Image.open("main/resources/Python-Emblem.png")
    linkedin_image = Image.open("main/resources/Python-Emblem.png")
    email_image = Image.open("main/resources/Python-Emblem.png")

    st.markdown("### Contact me! 📱")

    github_url = "https://github.com/tu_usuario"
    linkedin_url = "https://www.linkedin.com/in/tu_usuario"
    email_url = "mailto:tu_email@dominio.com"

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("", key="github_button", help="Visita mi GitHub"):
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="data:image/png;base64,{github_image}" style="border-radius:50%; width:100px; height:100px;"></a>', unsafe_allow_html=True)

    with col2:
        if st.button("", key="linkedin_button", help="Visita mi LinkedIn"):
            st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="data:image/png;base64,{linkedin_image}" style="border-radius:50%; width:100px; height:100px;"></a>', unsafe_allow_html=True)

    with col3:
        if st.button("", key="email_button", help="Enviar un email"):
            st.markdown(f'<a href="{email_url}" target="_blank"><img src="data:image/png;base64,{email_image}" style="border-radius:50%; width:100px; height:100px;"></a>', unsafe_allow_html=True)
