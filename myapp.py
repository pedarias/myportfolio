import streamlit as st
from PIL import Image
from Pages import home, project, contact, create
from streamlit_option_menu import option_menu

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Welcome to my Portfolio",
    page_icon="🐒",
)

# Optional: CSS and Logo
mystyle = '''
<style>
    p { text-align: justify; }
    .css-1vq4p4l { padding: 1.5rem 1rem 1.5rem; }
</style>
'''
st.markdown(mystyle, unsafe_allow_html=True)

# Load the logo image
logo = Image.open('/home/a10/Downloads/DALLog.webp')  # Adjust path as needed
st.sidebar.image(logo, use_column_width=True)

# Sidebar navigation using streamlit_option_menu
with st.sidebar:
    choose = option_menu("Main Menu", ["My Home Page", "My Projects", "About Me", "Create ML"],
                         icons=['house', 'book', 'person'],
                         menu_icon="cast", default_index=0,
                         styles={
    "container": {"padding": "0!important", "background-color": "#333333"},
    "icon": {"color": "white", "font-size": "25px"}, 
    "nav-link": {
        "font-size": "18px",
        "text-align": "left",
        "margin": "0px",
        "padding": "12px 16px",
        "color": "white",
        "--hover-color": "#555555"
    },
    "nav-link-selected": {
        "background-color": "#007BFF",
        "color": "white"
    }
})

# Page rendering based on sidebar navigation
if choose == "My Home Page":
    home.main()
elif choose == "My Projects":
    project.show_projects()
elif choose == "About Me":
    contact.show_contact()
elif choose == "Create ML":
    create.createML()

