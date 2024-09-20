import streamlit as st

def show_contact():
    # CSS styles file
    with open("styles/main.css") as f:
        main_css = f"<style>{f.read()}</style>"
        st.markdown(main_css, unsafe_allow_html=True)

    # About me section
    st.subheader("About Me")
    st.write("""
    - I am a **graduated Physicist** from the Universidade Estadual de Londrina (UEL), who has deepened in the Master's course in Computer Engineering at UTFPR-CP, thematic area Artificial Intelligence. My interest in switching my major from Physics to Computer Science was kindled by the great passion I have: applying abstract mathematical ideas to real problems in the industry.

        In my master's degree at HUB IA Senai, I work with projects in Data Science and Automation, which offer real solutions to the problems that customer companies go through. This position need continuous learning while using new technologies, of which I have become an expert in Python and SQL, among others. My work involves building machine learning models, web applications, conducting data studies, and automating processes through ETLs and webscraping.

        This amalgamation of academic rigor and practical application really goes on to underline my commitment toward making a mark in the industry not only by improving technical skills but also by contributing to them through innovation and development. Taking all this into consideration, I am devoted to constant professional development. I become active in courses, where I would like to widen my knowledge and improve competence in the fast-evolving tech landscape 🧑‍💻.
    
    - 📫 How to reach me: pedroarias92@gmail.com
    
    - 🏠 Londrina
    """)

    # Download CV button
    with open("assets/curricu.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="curricu.pdf",
        mime="application/pdf"
    )
