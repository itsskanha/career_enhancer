import streamlit as st
from github_analytics.fetch_data import fetch_user_data
from github_analytics.display_user_info import display_user_info
from github_analytics.pie_chart import create_pie_chart
from github_analytics.line_chart import create_line_chart
from github_analytics.bubble_chart import create_bubble_chart
from github_analytics.bar_chart import create_bar_chart


def github_analytics():
    """Streamlit app for fetching and displaying GitHub user and repository data."""
    st.title("Github Analytics")
    username = st.text_input("Enter your GitHub username")
    if username:
        user_data, repo_data = fetch_user_data(username)
        if user_data == "User not found":
            st.error("User not found")
            return

        if repo_data == "Repo not found":
            st.write("Repo not found")
            return

        if user_data:
            if repo_data:
                display_user_info(user_data)
                # st.write("**User Info:**")
                # st.write(user_data)
                # st.write("**Repo Info:**")
                # st.write(repo_data)

                st.title("Select a metric to analyze")
                option = st.selectbox(
                    "",
                    ("Stars", "Forks", "Languages Used",
                     "Stars and Forks compared with time"),
                    index=None,
                    placeholder="Select something...",
                )

                st.write("You selected:", option)

                # Dictionary to map options to functions
                option_functions = {
                    "Stars": create_bar_chart,
                    "Forks": create_line_chart,
                    "Languages Used": create_pie_chart,
                    "Stars and Forks compared with time": create_bubble_chart,
                }

                # Call the corresponding function based on the selected option
                if option in option_functions:
                    option_functions[option](repo_data)
                else:
                    st.warning("Invalid option selected.")

            else:
                st.error(f"No repositories found for the user '{username}'.")
        else:
            st.title(f"Invalid username '{username}'. Please enter a valid GitHub username.")
