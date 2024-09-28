import streamlit as st
import requests
from PIL import Image
import base64
from streamlit_lottie import st_lottie

def main():
    # Carregar o CSS
    with open("styles/main.css") as f:
        main_css = f"<style>{f.read()}</style>"
        st.markdown(main_css, unsafe_allow_html=True)

    # Carregar e exibir imagem de perfil
    with open("assets/me.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # Display profile image and title
    st.markdown("<h1 style='text-align: center; color: #0000FF;'>Welcome to my Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Hello! My name is Pedro</h3>", unsafe_allow_html=True)

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
    """, unsafe_allow_html=True)

    # Animações Lottie
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

    # Social Icons
    social_icons_data = {
        "LinkedIn": ["https://linkedin.com/in/pedroarias92", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/pedarias", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank'><img src='{social_icons_data[platform][1]}' width='25'></a>" for platform in social_icons_data]
    st.write(f"<div style='display: flex; justify-content: center;'>{''.join(social_icons_html)}</div>", unsafe_allow_html=True)

    st.write("## Explore My Projects!")
    st.write("Check out the 'Projects' section to see detailed descriptions of the work I have done so far.")
