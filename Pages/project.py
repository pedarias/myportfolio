import streamlit as st
from PIL import Image


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
    company = st.radio(
        "Selecione a empresa para ver os projetos",
        ["Trimble", "AGCO", "IST", "UFV"]
    )

    if company == "Trimble":
        show_trimble_projects()
    elif company == "AGCO":
        show_agco_projects()
    elif company == "IST":
        show_ist_projects()
    elif company == "UFV":
        show_ufv_projects()

# Projetos da empresa Trimble
def show_trimble_projects():
    st.markdown("# Projeto Trimble Transportation - HUB-IA SENAI")
    
    st.image("assets/Trimble-logo.png", caption="Trimble", width=200)
    
    st.markdown("""
    ## Sobre a Empresa

    **Trimble Transportation** é uma divisão da **Trimble Inc.**, especializada em soluções tecnológicas para o setor de transporte e logística. Seu foco é fornecer ferramentas inovadoras que aumentem a eficiência operacional e a segurança na gestão de frotas. Durante a parceria com o **HUB de IA do SENAI**, foram desenvolvidas Provas de Conceito (POCs) estruturadas em 4 Sprints.

    ---
    """)

    st.markdown("""
    ### POC 1: Análise e Predição de Dados na Gestão de Frotas

    #### Objetivo
    Desenvolver uma solução para análise exploratória de dados, predição e segmentação de padrões operacionais usando **Machine Learning**, visando a identificação de padrões relacionados à fadiga de motoristas.

    #### Tecnologias Utilizadas
    - **Visualização de Dados**: Matplotlib, Plotly
    - **Ciência de Dados**: Pandas, SciPy, PySpark
    - **Machine Learning**: Scikit-Learn

    #### Descrição do Projeto
    - **Sprint 1**: Realizamos uma análise exploratória dos dados fornecidos pela Trimble, buscando identificar padrões de uso na plataforma da empresa. Para isso, desenvolvemos um **dashboard interativo em Streamlit**, permitindo a visualização e filtragem dos dados de forma eficiente e dinâmica.
    
    - **Sprint 2**: O foco foi identificar padrões relacionados à **fadiga dos motoristas**. Utilizando **Big Data** com **PySpark**, aplicamos técnicas de **clusterização**, como **K-means** e **DBSCAN**, para segmentar os dados. Em seguida, modelos preditivos como **Random Forest** foram usados para prever situações de fadiga. Os resultados incluíram a identificação de clusters operacionais, correlacionando variáveis que contribuem para o aumento da fadiga.
    """)
    
    st.image("assets/PCA.png", caption="Resultados da Análise PCA", width=400)

    st.markdown("""
    ---
    ### POC 2: Identificação e Segmentação de Objetos Soltos e Classificação de Chuva

    #### Objetivo
    Aplicar técnicas de **Visão Computacional** para identificar objetos soltos nas cabines dos veículos e desenvolver um classificador de condições climáticas adversas, focado na detecção de chuva.

    #### Tecnologias Utilizadas
    - **Visualização de Dados**: Matplotlib, Plotly
    - **Deep Learning**: PyTorch, Keras, TensorFlow

    #### Descrição do Projeto
    - **Sprint 3**: O foco foi **detectar e segmentar objetos soltos**. Implementamos o modelo **YOLOv9-SEG** para segmentação, além disso, utilizamos as arquiteturas de **GroundingDINO** e **Segment Anything Model (SAM)** para a detecção e segmentação **zero-shot** de novos objetos sem necessidade de re-treinamento, que visa detectar e segmentar qualquer coisa através de textos!

    - **Sprint 4**: Desenvolvemos um **classificador de condições de chuva** baseado em imagens capturadas por câmeras veiculares. O modelo foi construído utilizando redes neurais convolucionais (**CNN**) com **Transfer Learning** e **Fine Tuning**, ajustando modelos pré-treinados ao nosso dataset específico. Para mitigar **Overfitting**, utilizamos camadas de regularização e **callbacks** para monitorar a performance do modelo no conjunto de validação. O modelo final apresentou melhora significativa na acurácia no conjunto de teste, comparado com o modelo sem regularizadores (sem métodos para prevenir overfitting), mostrando que o modelo é capaz de Generalizar melhor.
    """)

    st.image("assets/EnsembleTransferLearning.png", caption="Transfer Learning para Classificação de Imagens", width=400)
    st.markdown("*Fonte Imagem: [Ensemble Transfer Learning Framework for Vessel Size Estimation from 2D Images](https://www.researchgate.net/publication/333619654_Ensemble_Transfer_Learning_Framework_for_Vessel_Size_Estimation_from_2D_Images)*")


# Projetos da empresa AGCO
def show_agco_projects():
    st.markdown("# Projeto AGCO - HUB-IA SENAI")

    st.image("assets/AGCO-descript-logo.png", caption="AGCO", width=400)

    st.markdown("""
    ## Sobre o Projeto

    Este projeto foi desenvolvido durante minha residência no **HUB de IA do SENAI** e visa identificar e analisar inconsistências entre diferentes bases de dados da **AGCO**, uma das maiores fabricantes de equipamentos agrícolas do mundo. 
    O objetivo central foi a criação de uma solução que automatizasse a detecção de discrepâncias nos dados provenientes da empresa. 
    
    Para isso, foi desenvolvido um **pipeline de ETL** capaz de extrair diversos formatos de dados, transformá-los e armazená-los em um banco de dados **PostgreSQL**. Além disso, uma **API** foi implementada utilizando **FastAPI** para facilitar a interação entre o frontend e backend, enquanto a interface do usuário foi criada em **Streamlit** para possibilitar o upload e a visualização das análises num Dashboard.

    ---
    """)

    st.image("assets/etlpipelineagco.png", caption="ETL Pipeline", width=600)

    st.markdown("""
    ## Arquitetura do Sistema

    - **ETL Pipeline**: Automação completa para extração, transformação e carregamento dos dados em diferentes formatos, com armazenamento no banco de dados **PostgreSQL**.
    - **FastAPI**: API responsável pelas operações CRUD no banco de dados, atuando como intermediário entre o frontend e o backend.
    - **Streamlit**: Interface gráfica desenvolvida para permitir que o usuário faça upload de arquivos, visualize dados e análises de inconsistências.
    - **Docker**: Containerização dos componentes do sistema, garantindo consistência entre os ambientes de desenvolvimento e produção e escalabilidade.

    ---
    """)

    st.image("assets/agcoarquitetura.png", caption="Arquitetura do Sistema", width=400)

    st.markdown("""
    ## Funcionalidades

    - **Identificação de Divergências**
    - **Verificação de Registros Temporais**
    - **Análise Geográfica**
    - **Análise Exploratória dos Dados**

    ---
    """)

    st.markdown("""
    ## Tecnologias Utilizadas

    - **Python**: Linguagem principal usada para o backend e processamento dos dados.
    - **FastAPI**: Framework utilizado para a criação da API, facilitando a comunicação entre o frontend e o backend.
    - **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados processados.
    - **Streamlit**: Framework para construção da interface gráfica que permite interações e visualização dos dados de forma intuitiva.
    - **Docker**: Ferramenta utilizada para containerização e padronização do ambiente de desenvolvimento e produção.

    ---
    """)

    # Inclui imagens e outros recursos
    st.image("assets/etlpipelineagco.png", caption="Pipeline de ETL para o Projeto AGCO", use_column_width=True)


# Projetos da empresa IST
def show_ist_projects():
    st.markdown("# Otimização de Parâmetros em Modelo de Circuito Equivalente Utilizando Algoritmo de Evolução")

    st.image("assets/ISTarq.png", caption="Pipeline do Projeto de Otimização de Parâmetros", use_column_width=True)

    st.markdown("""
    ## Sobre o Projeto

    Este projeto foi desenvolvido para o **Instituto SENAI de Tecnologia e Inovação** com o objetivo de ajustar os parâmetros de modelos de circuitos equivalentes para que estes se comportem de maneira semelhante aos dados experimentais de **Espectroscopia de Impedância Eletroquímica (EIS)**. Utilizando uma abordagem de otimização, o projeto visa melhorar a acurácia dos modelos simulados ao ajustar seus parâmetros com base em dados reais.

    ---
    """)

    st.markdown("""
    ## Objetivos

    - Propor uma metodologia eficiente para ajustar os parâmetros de circuitos equivalentes a partir de dados experimentais de EIS.
    - Utilizar algoritmos de otimização para encontrar os parâmetros que melhor se ajustem aos dados experimentais.

    ---
    """)

    st.markdown("""
    ## Escopo

    O projeto envolve a modelagem de sistemas eletroquímicos a partir de dados de EIS, utilizando técnicas avançadas de ajuste de parâmetros e otimização para aprimorar os modelos de circuitos equivalentes.

    ---
    """)

    st.markdown("""
    ## Tecnologias Utilizadas

    - **Análise de Dados**: Python, Pandas, SciPy
    - **Algoritmos de Otimização**: Evolução Diferencial
    - **Visualização**: Pyplot para geração de gráficos de Nyquist

    ---
    """)

    st.markdown("""
    ## Metodologia

    Os dados de EIS fornecidos pelo IST foram pré-processados e analisados para extrair as características relevantes dos sistemas eletroquímicos. Esses dados permitiram a formulação dos modelos de circuito equivalente, utilizados para simular o comportamento do sistema.

    ### Otimização

    O algoritmo de **Evolução Diferencial** foi aplicado para otimizar os parâmetros dos modelos de circuito equivalente. A função de custo foi definida para minimizar o erro entre os valores simulados e os dados experimentais, assegurando que os modelos ajustados refletissem com precisão o comportamento eletroquímico dos sistemas.

    ### Visualização

    Para verificar a precisão dos ajustes, **gráficos de Nyquist** foram gerados, permitindo uma comparação visual entre os dados experimentais e os dados simulados dos modelos ajustados. Estes gráficos são fundamentais para avaliar a adequação dos modelos otimizados.

    ---
    """)

    st.image("assets/ISTarq.png", caption="Pipeline do Projeto", use_column_width=True)

    st.markdown("""
    ## Resultados

    Os resultados obtidos demonstraram a eficácia do algoritmo de **Evolução Diferencial** na otimização dos parâmetros dos circuitos equivalentes, com uma significativa redução no erro entre os dados simulados e experimentais. Através da visualização gráfica dos dados, foi possível validar a acurácia dos modelos.

    ---
    """)

    st.markdown("""
    ## Próximos Passos

    O próximo passo é explorar a aplicação de **redes neurais** para a otimização dos parâmetros em futuras iterações, com o objetivo de melhorar ainda mais a precisão dos modelos ajustados.

    ---
    """)

    st.markdown("""
    ## Contato

    ##### Pedro Henrique Arias Oliveira:
    <p align="center"> 
      <a href="https://www.linkedin.com/in/pedroarias92/" target="_blank">
        <img align="center" src="https://logosmarcas.net/wp-content/uploads/2020/04/Linkedin-Logo.png" height="30" />
      </a> 
      <a href="mailto:pedro.oliveira@sistemafiep.org.br" target="_blank">
        <img align="center" src="https://w7.pngwing.com/pngs/995/259/png-transparent-microsoft-outlook-logo-outlook-com-microsoft-outlook-email-microsoft-office-365-outlook-miscellaneous-blue-text.png" height="30" />
      </a>
    </p>
    """, unsafe_allow_html=True)

# Projetos da Universidade Federal de Viçosa
def show_ufv_projects():
    st.markdown("# Projeto Universidade Federal de Viçosa - HUB-IA SENAI")

    st.image("assets/UFV-logo.png", caption="Universidade Federal de Viçosa", width=200)

    st.markdown("""
    ## Aplicação de Modelos de Detecção de Objetos para Identificação de Macacos em Imagens e Vídeos

    ### Objetivo
    Desenvolver modelos de visão computacional para detectar e identificar macacos em imagens e vídeos, utilizando técnicas avançadas de **Inteligência Artificial** e **Aprendizado de Máquina**.

    ### Tecnologias Utilizadas
    - **Visão Computacional**: OpenCV
    - **Deep Learning**: PyTorch
    - **Modelos de Detecção de Objetos**: YOLOv8, Detectron2
    - **Ferramentas de Anotação de Dados**: Roboflow
    - **Linguagem de Programação**: Python

    ### Descrição do Projeto
    O projeto envolveu o desenvolvimento e a comparação de diferentes modelos de detecção de objetos para identificar macacos em imagens capturadas por câmeras térmicas. Foram utilizadas técnicas de **Deep Learning**, incluindo Redes Neurais Convolucionais e algoritmos de detecção como o **YOLOv8** e o **Detectron2**.

    #### Pré-processamento e Anotação de Dados
    - Utilização de ferramentas como o **Roboflow** para anotação e preparação dos datasets.
    - Conversão dos dados para formatos adequados para cada modelo, como o formato **COCO** para o Detectron2.

    #### Desenvolvimento dos Modelos
    - **Detectron2**: Implementação e treinamento do modelo para detecção de objetos, explorando diferentes hiperparâmetros.
    - **YOLOv8**: Treinamento do modelo **YOLOv8**, que apresentou melhor desempenho na detecção dos macacos.

    #### Resultados
    - O modelo **YOLOv8** conseguiu detectar macacos em imagens térmicas com alta precisão, demonstrando a eficácia das técnicas de **Deep Learning** aplicadas.
    - Foram gerados gráficos de perda e métricas de desempenho para avaliar a evolução do treinamento.

    ### Próximos Passos
    - Otimização dos hiperparâmetros do modelo para melhorar a precisão.
    - Aumentar a variedade e quantidade de dados de treinamento, incluindo imagens de fundo sem macacos, para reduzir falsos positivos.
    - Desenvolvimento de uma interface de usuário para facilitar o teste e a aplicação do modelo em diferentes tipos de imagens.

    """)


# Função para exibir os projetos pessoais
def show_personal_projects():
    st.markdown("### Meus Projetos Pessoais se encontram no meu Github. Para acessá-los clique no logo abaixo:")
    # Ícone do GitHub com link para o repositório
    social_icons_data = {
        "GitHub": ["https://github.com/pedarias", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank'><img src='{social_icons_data[platform][1]}' width='50'></a>" for platform in social_icons_data]
    st.write(f"<div style='display: flex; justify-content: center;'>{''.join(social_icons_html)}</div>", unsafe_allow_html=True)

# Função principal que pode ser chamada no app
if __name__ == "__main__":
    show_projects()
