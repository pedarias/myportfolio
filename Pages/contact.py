import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie

def show_contact():    
    # CSS styles for button
    button_style = """
<style>
/* Target the button by testid for consistency */
button[data-testid='baseButton-secondary']:hover {
    background-color: #4CAF50; /* Green */
    color: white; /* Ensure text color is white on hover for better visibility */
}
</style>
"""
    st.markdown(button_style, unsafe_allow_html=True)


    
    # CSS styles file
    with open("styles/main.css") as f:
        main_css = f"<style>{f.read()}</style>"
        st.markdown(main_css, unsafe_allow_html=True)
    # Profile image file
    with open("assets/me.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
    # PDF CV file
    with open("assets/curricu.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hello! My name is</strong> Pedro</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Pedro H. Arias Oliveira">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Load and display Lottie animations
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_urls = {
        "python": "https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json",
        "java": "https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json",
        "my_sql": "https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json",
        "git": "https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json",
        "github": "https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json",
        "docker": "https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json",
        "figma": "https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json",
        "js": "https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json"
    }

    lottie_animations = {key: load_lottieurl(url) for key, url in lottie_urls.items()}
    with st.container():
        st.subheader('Skills')
        cols = st.columns(len(lottie_animations))
        for col, (key, animation) in zip(cols, lottie_animations.items()):
            with col:
                if animation:
                    st_lottie(animation, height=150, key=key)

    # Social Icons and other sections
    # (The rest of your contact.py code here...)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Data Scientist | AI Specialist</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://linkedin.com/in/pedroarias92", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/pedarias", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - I am a **graduated Physicist** from the Universidade Estadual de Londrina (UEL), who has deepened in the Master's course in Computer Engineering at UTFPR-CP, thematic area Artificial Intelligence. My interest in switching my major from Physics to Computer Science was kindled by the great passion I have: applying abstract mathematical ideas to real problems in the industry.

        In my master's degree at HUB IA Senai, I work with projects in Data Science and Automation, which offer real solutions to the problems that customer companies go through. This position need continuous learning while using new technologies, of which I have become an expert in Python and SQL, among others. My work involves building machine learning models, web applications, conducting data studies, and automating processes through ETLs and webscraping.

        This amalgamation of academic rigor and practical application really goes on to underline my commitment toward making a mark in the industry not only by improving technical skills but also by contributing to them through innovation and development. Taking all this into consideration, I am devoted to constant professional development. I become active in courses, where I would like to widen my knowledge and improve competence in the fast-evolving tech landscape 🧑‍💻.
    
    - 📫 How to reach me: pedroarias92@gmail.com
    
    - 🏠 Londrina
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="curricu.pdf",
        mime="application/pdf"
    )

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)
