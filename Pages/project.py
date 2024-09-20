import streamlit as st

def show_projects():
    # Carregar o CSS
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Menu principal para selecionar tipo de projeto
    project_type = st.selectbox(
        "Selecione o tipo de projeto",
        ["HUB-IA Projects", "Personal Projects"]
    )

    if project_type == "HUB-IA Projects":
        show_hub_ia_projects()  # Mostra os projetos do HUB-IA
    elif project_type == "Personal Projects":
        show_personal_projects()  # Mostra os projetos pessoais

# Função para exibir os projetos HUB-IA com submenu de empresas
def show_hub_ia_projects():
    # Exibição da descrição do repositório HUB-IA
    st.markdown("# Repositório HUB-IA SENAI")
    st.image("assets/Residência-IA.jpeg", width=400, caption="Residência IA")
    
    st.markdown("""
    ## Sobre o HUB-IA
    Este repositório reúne uma seleção de projetos desenvolvidos durante minha residência no HUB de Inteligência Artificial (HUB-IA) do SENAI, em parceria com diversas empresas do setor industrial e de tecnologia. Esses projetos foram projetados para enfrentar problemas reais e complexos, abrangendo desde a otimização de processos industriais até a implementação de soluções inovadoras baseadas em Inteligência Artificial (IA) e análise avançada de dados.

    Por meio da aplicação de metodologias de Machine Learning, Visão Computacional, Big Data e outras tecnologias emergentes, os projetos entregam soluções tangíveis que ajudam as empresas parceiras a resolver desafios operacionais e estratégicos. Cada projeto foi desenvolvido em estreita colaboração com as empresas, com foco na criação de valor e inovação tecnológica.

    > **Nota**: Os conteúdos dos projetos são limitados a descrições gerais, sendo os dados e o código-fonte confidenciais. Informações detalhadas estão disponíveis apenas conforme os termos dos acordos de confidencialidade.

    ## Aviso Legal
    Os projetos destinam-se exclusivamente para documentação e apresentação de metodologias utilizadas nos projetos. Qualquer conteúdo aqui presente foi revisado para atender aos requisitos de confidencialidade. 
    Não estão inclusos dados sensíveis, códigos proprietários ou qualquer informação que possa comprometer a privacidade das empresas parceiras.

    Para mais informações sobre os projetos ou para esclarecimentos adicionais, entre em contato diretamente.
    """)

    # Seleção da empresa dentro dos projetos HUB-IA
    company = st.selectbox(
        "Selecione a empresa para ver os projetos",
        ["Trimble", "AGCO", "IST"]
    )

    if company == "Trimble":
        show_trimble_projects()
    elif company == "AGCO":
        show_agco_projects()
    elif company == "IST":
        show_ist_projects()

# Projetos da empresa Trimble
def show_trimble_projects():
    st.markdown("### Trimble Transportation - Análise e Predição de Dados na Gestão de Frotas")
    st.markdown("""
    - **Descrição**: Este projeto visa a análise exploratória de dados e predição de padrões operacionais relacionados à fadiga dos motoristas. Utilizamos técnicas de Big Data e Machine Learning para segmentação e predição de variáveis operacionais críticas.
    - **Tecnologias Usadas**: Pandas, PySpark, Scikit-Learn, Matplotlib, Plotly
    """)
    st.image("assets/PCA.png", caption="Resultados da Análise PCA", width=400)

    st.markdown("### Trimble Transportation - Identificação e Segmentação de Objetos e Classificação de Chuva")
    st.markdown("""
    - **Descrição**: Projeto de visão computacional com foco na segurança e organização das cabines dos veículos. Desenvolvemos também um classificador de condições climáticas baseado em imagens.
    - **Tecnologias Usadas**: PyTorch, TensorFlow, Keras, Matplotlib, Plotly
    """)
    st.image("assets/EnsembleTransferLearning.png", caption="Transfer Learning para Classificação de Imagens", width=400)

# Projetos da empresa AGCO
def show_agco_projects():
    st.markdown("### AGCO - Identificação de Inconsistências em Bases de Dados")
    st.markdown("""
    - **Descrição**: Este projeto visa identificar e analisar inconsistências entre diferentes bases de dados da empresa AGCO. Um pipeline de ETL foi desenvolvido para processamento de dados.
    - **Tecnologias Usadas**: Python, FastAPI, PostgreSQL, Streamlit, Docker
    """)
    st.image("assets/agcoarquitetura.png", caption="Arquitetura do Sistema AGCO", width=400)
    st.image("assets/etlpipelineagco.png", caption="Pipeline de ETL para o Projeto AGCO", use_column_width=True)

# Projetos da empresa IST
def show_ist_projects():
    st.markdown("### IST - Otimização de Parâmetros em Modelo de Circuito Equivalente")
    st.markdown("""
    - **Descrição**: Este projeto foi desenvolvido para ajustar os parâmetros de modelos de circuitos equivalentes com base em dados experimentais de Espectroscopia de Impedância Eletroquímica (EIS).
    - **Tecnologias Usadas**: Python, Pandas, SciPy, Evolução Diferencial, Pyplot
    """)
    st.image("assets/ISTarq.png", caption="Pipeline do Projeto de Otimização de Parâmetros", use_column_width=True)

# Função para exibir os projetos pessoais
def show_personal_projects():
    st.markdown("### Meus Projetos Pessoais")
    st.markdown("""
    Aqui estão alguns dos meus projetos pessoais, desenvolvidos fora do contexto do HUB-IA.
    """)
    # Adicione detalhes dos seus projetos pessoais aqui
    st.markdown("### Projeto Pessoal 1: [Título do Projeto]")
    st.markdown("""
    - **Descrição**: Descrição breve do projeto pessoal.
    - **Tecnologias Usadas**: [Tecnologias]
    """)
    st.markdown("### Projeto Pessoal 2: [Título do Projeto]")
    st.markdown("""
    - **Descrição**: Descrição breve do projeto pessoal.
    - **Tecnologias Usadas**: [Tecnologias]
    """)

# Função principal que pode ser chamada no app
if __name__ == "__main__":
    show_projects()
