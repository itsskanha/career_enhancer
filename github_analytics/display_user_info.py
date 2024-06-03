import streamlit as st


def display_user_info(user_data):
    """Displays user information retrieved from GitHub API."""
    if not user_data:
        return

    st.title("**User Info:**")

    st.write(f"**Name:** {user_data['name']}")
    st.write(f"**Username:** {user_data['login']}")

    st.write("**User Image:**")
    st.image(user_data["avatar_url"], width=100)

    bio = user_data.get("bio", "N/A")
    location = user_data.get("location", "N/A")
    st.write(f"**Bio:** {bio}")
    st.write(f"**Location:** {location}")

    st.write("---")  # Separator

    st.metric("Repositories", user_data["public_repos"])
    st.metric("Followers", user_data["followers"])
    st.metric("Following", user_data["following"])
