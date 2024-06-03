import streamlit as st
import plotly.graph_objs as go
from github_analytics.singular_analysis_chat import predict_2vars


def create_bar_chart(repo_data):
    st.subheader("Here's your data visualization of Repositories compared by stars:")
    # Extract labels and data from repo_data
    if not repo_data:
        return None

    labels = [repo['name'] for repo in repo_data]
    stars = [repo['stargazers_count'] for repo in repo_data]

    # Create a Plotly line chart
    fig = go.Figure(data=go.Bar(x=labels, y=stars))

    # Customize the chart
    fig.update_layout(
        title='Stars by Repository',
        xaxis_title='Repository',
        yaxis_title='Number of Stars',
        hovermode='closest',
        xaxis=dict(tickangle=-45), # Rotate x-axis labels
        width=800,  # Set desired width
        height=600
    )

    # Customize hover label
    fig.update_traces(
        hovertemplate='Repository: %{x}<br>Forks: %{y}'
    )
    response = predict_2vars(labels, stars, "repo names", "stars")
    return st.plotly_chart(fig), st.write(response)
