import streamlit as st

def show_projects():

    # Load CSS
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Projects Introduction
    st.markdown("## My Projects")
    st.markdown("""
    Here are some of the projects I have worked on. Click on each project for more details!
    """)
    
    # Example Project 1
    st.markdown("### Project 1: Data Visualization App")
    st.markdown("""
    - **Description**: This project showcases an interactive data visualization app built with Streamlit that allows users to explore various datasets and their insights.
    - **Technologies Used**: Python, Streamlit, Pandas, Plotly
    - **[More Details](link-to-your-project-details)**
    """)

    # Example Project 2
    st.markdown("### Project 2: Machine Learning Model")
    st.markdown("""
    - **Description**: Developed a machine learning model to predict stock prices based on historical data.
    - **Technologies Used**: Python, Scikit-Learn, NumPy, Matplotlib
    - **[More Details](link-to-your-project-details)**
    """)

    # Add more projects as needed

