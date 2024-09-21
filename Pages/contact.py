import streamlit as st

def show_contact():
    # CSS styles file
    with open("styles/main.css") as f:
        main_css = f"<style>{f.read()}</style>"
        st.markdown(main_css, unsafe_allow_html=True)

    # About me section
    st.subheader("About Me")
    st.write("""
    - Sou bacharel em Física pela UEL (Universidade Estadual de Londrina) e, ao longo da minha formação, desenvolvi habilidades sólidas de pensamento lógico que podem ser aplicadas de maneira eficaz no campo da Ciência da Computação. Ao realizar à transição da Física para a Ciência da Computação, percebi que eu gostaria de continuar estudando matemática abstrata mas aplicá-la em algo mais concreto, no mercado de trabalho por exemplo.

Sou aluno regular do Programa de Pós-Graduação em Informática (PPGI) da UTFPR-CP (Universidade Tecnológica Federal do Paraná - Câmpus Cornélio Procópio). É um mestrado integrado com o programa de Residência em Inteligência Artificial no HUB-IA SENAI, no qual desenvolvemos projetos e soluções inovadoras para empresas clientes do programa, lidando diretamente com problemas reais.
Atualmente, atuo como **Cientista de Dados Jr** no SENAI onde busco participar dos mais diversos projetos possíveis, com o objetivo de ampliar meus conhecimentos e ganhar experiência na área. Estou comprometido com o aprendizado contínuo e entusiasmado em aplicar minhas habilidades para solucionar problemas práticos no mercado de trabalho.
    
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
