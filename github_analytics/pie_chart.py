import streamlit as st
from github_analytics.singular_analysis_chat import predict_2vars
import plotly.graph_objs as go


def create_pie_chart(repo_data):
    """Creates an interactive pie chart showing the distribution of repository languages."""
    if not repo_data:
        return None

    languages = {}
    for repo in repo_data:
        if repo.get("language"):  # Check if language exists
            languages[repo["language"]] = languages.get(repo["language"], 0) + 1

    language_labels = list(languages.keys())
    language_counts = list(languages.values())

    if not language_labels:
        st.write("No languages found in repositories.")
        return None

    # Create Plotly pie chart
    fig = go.Figure(data=[go.Pie(labels=language_labels, values=language_counts)])

    fig.update_layout(
        title="Repository Language Distribution",
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        ),
        width=800,
        height=600
    )

    response = predict_2vars(language_labels, language_counts, "language_labels", "language_counts")
    return st.plotly_chart(fig), st.write(response)
