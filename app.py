import streamlit as st
from streamlit_option_menu import option_menu
from github_analytics.home import github_analytics
from project_recommender.app import project_recommendation
from home_page import home_page

# Set the layout to make the navigation menu appear sideways
st.set_page_config(layout="wide")

# Create a sidebar for the navigation menu
with st.sidebar:
    # Navigation menu
    selected_page = option_menu(
        menu_title="Career Enhancer",
        options=["Home", "Github Analytics", "Custom Project Recommendation"],
        icons=["house", "github", "star"],  # Optional icons
        default_index=0,  # Set the default option to "Home"
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Create a container for the main content area
main_content = st.container()

# Display content based on selection
if selected_page == "Home":
    with main_content:
        home_page()
elif selected_page == "Github Analytics":
    with main_content:
        github_analytics()
elif selected_page == "Custom Project Recommendation":
    with main_content:
        project_recommendation()
