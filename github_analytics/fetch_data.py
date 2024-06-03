import streamlit as st
import requests


def fetch_user_data(username):
    """Fetches user and repository data from GitHub API."""
    loading = st.empty()  # Placeholder for loading indicator
    error = st.empty()  # Placeholder for error message

    try:
        user_response = requests.get(f"https://api.github.com/users/{username}")
        user_data = user_response.json()

        # Check if the user data contains a 'message' key indicating user not found
        if 'message' in user_data and user_data['message'] == 'Not Found':
            loading.empty()  # Remove loading indicator
            return "User not found", "Repo not found"

        repo_response = requests.get(f"https://api.github.com/users/{username}/repos")
        repo_data = repo_response.json()

        loading.empty()  # Remove loading indicator
        return user_data, repo_data

    except requests.exceptions.RequestException as e:
        error.text = f"Error: {e}"
        loading.empty()  # Remove loading indicator
        return None, None
