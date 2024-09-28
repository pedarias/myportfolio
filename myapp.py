import streamlit as st
from PIL import Image
from Pages import home, project, contact
from streamlit_option_menu import option_menu

# 1. Chame `st.set_page_config` imediatamente após `import streamlit`
st.set_page_config(
    page_title="Welcome to my Portfolio",
    page_icon="🐒",
)

# 2. Defina estilos personalizados após `set_page_config`
mystyle = '''
<style>
    p { text-align: justify; }
    .css-1vq4p4l { padding: 1.5rem 1rem 1.5rem; }
</style>
'''
st.markdown(mystyle, unsafe_allow_html=True)

# 3. Carregue o logo e configure a barra lateral
logo = Image.open('./assets/Dall-e.webp')  # Certifique-se de que o caminho está correto
st.sidebar.image(logo, use_column_width=True)

# 4. Menu de navegação na barra lateral
with st.sidebar:
    choose = option_menu("Main Menu", ["My Home Page", "My Projects", "About Me"],
                         icons=['house', 'book', 'person'],
                         menu_icon="cast", default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#333333"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {"font-size": "18px", "color": "white", "--hover-color": "#555555"},
        "nav-link-selected": {"background-color": "#007BFF", "color": "white"}
    })

# 5. Rotear entre as páginas
if choose == "My Home Page":
    home.main()
elif choose == "My Projects":
    project.show_projects()
elif choose == "About Me":
    contact.show_contact()
