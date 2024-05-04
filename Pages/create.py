import streamlit as st
import pandas as pd
import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def createML():
    # Set up the customization options
    st.sidebar.title('Customization')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama3-8b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it']
    )

    llm = ChatGroq(
        temperature=0, 
        groq_api_key=os.environ['GROQ_API_KEY'], 
        model_name=model
    )

    # Streamlit UI setup
    st.title("Welcome to My Portfolio!")
    st.markdown("""
        Welcome! I'm here to guide you through my projects and expertise in machine learning. You can ask about my work, 
        the technologies I use, or even get help starting your own ML project.
        """, unsafe_allow_html=True)

    # Displaying the logo
    spacer, col = st.columns([5, 1])  
    with col:  
        st.image('/home/a10/Downloads/DALLog.webp')  # Update path to your logo

    # Setting up AI agents for interactive responses
    Problem_Definition_Agent = Agent(
        role='Problem_Definition_Agent',
        goal="Clarify the machine learning problem the visitor wants to solve.",
        backstory="Expert in understanding and defining ML problems.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Data_Assessment_Agent = Agent(
        role='Data_Assessment_Agent',
        goal="Evaluate the visitor's data, assessing its quality and suitability.",
        backstory="Specializes in data evaluation and preprocessing.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Model_Recommendation_Agent = Agent(
        role='Model_Recommendation_Agent',
        goal="Suggest suitable ML models based on the problem definition and data assessment.",
        backstory="Expert in ML algorithms.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Starter_Code_Generator_Agent = Agent(
        role='Starter_Code_Generator_Agent',
        goal="Generate starter Python code for the project.",
        backstory="Able to generate starter code templates.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    user_question = st.text_input("Describe your ML problem:")
    data_upload = False
    uploaded_file = st.file_uploader("Upload a sample .csv of your data (optional)")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file).head(5)
            data_upload = True
            st.write("Data successfully uploaded and read as DataFrame:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading the file: {e}")

    if user_question:
        tasks = [Task(
            description=f"Clarify and define the machine learning problem based on the user's input: '{user_question}'",
            agent=Problem_Definition_Agent,
            expected_output="A clear and concise definition of the machine learning problem."
        )]

        if data_upload:
            tasks.append(Task(
                description=f"Evaluate the uploaded data for quality and suitability.",
                agent=Data_Assessment_Agent,
                expected_output="An assessment of the data's quality and suitability."
            ))

        tasks.append(Task(
            description="Suggest suitable machine learning models for the defined problem and assessed data.",
            agent=Model_Recommendation_Agent,
            expected_output="A list of suitable machine learning models."
        ))

        tasks.append(Task(
            description="Generate starter Python code tailored to the user's project.",
            agent=Starter_Code_Generator_Agent,
            expected_output="Python code snippets for the user's project."
        ))

        crew = Crew(
            agents=[Problem_Definition_Agent, Data_Assessment_Agent, Model_Recommendation_Agent, Starter_Code_Generator_Agent],
            tasks=tasks,
            verbose=2
        )

        result = crew.kickoff()
        st.write(result)
