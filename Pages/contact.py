import streamlit as st


# Função principal para a seção de contato
def show_contact():
    # Carregar o CSS
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Seção "About Me"
    st.subheader("About Me")
    st.write("""
    - Sou bacharel em Física pela UEL (Universidade Estadual de Londrina) e, ao longo da minha formação, desenvolvi habilidades sólidas de pensamento lógico que podem ser aplicadas de maneira eficaz no campo da Ciência da Computação. Ao realizar à transição da Física para a Ciência da Computação, percebi que eu gostaria de continuar estudando matemática abstrata mas aplicá-la em algo mais concreto, no mercado de trabalho por exemplo.

    - Sou aluno regular do Programa de Pós-Graduação em Informática (PPGI) da UTFPR-CP (Universidade Tecnológica Federal do Paraná - Câmpus Cornélio Procópio). É um mestrado integrado com o programa de Residência em Inteligência Artificial no HUB-IA SENAI, no qual desenvolvemos projetos e soluções inovadoras para empresas clientes do programa, lidando diretamente com problemas reais. Além disso, estou em processo de escrita da minha dissertação, o que tem me permitido aprofundar ainda mais na área de visão computacional.

    - Atualmente, atuo como **Cientista de Dados Jr** no SENAI onde busco participar dos mais diversos projetos possíveis, com o objetivo de ampliar meus conhecimentos e ganhar experiência na área. Estou comprometido com o aprendizado contínuo e entusiasmado em aplicar minhas habilidades para solucionar problemas práticos no mercado de trabalho.
    
    - 📫 Como me contactar: pedroarias92@gmail.com
    
    - 🏠 Londrina    """)

    # Botão para baixar o CV
    with open("assets/curricu.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="curricu.pdf",
        mime="application/pdf"
    )

    # Botão para exibir o formulário de contato

