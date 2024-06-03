import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from github_analytics.singular_analysis_chat import predict_df


def create_bubble_chart(repo_data):
    # Extract data from repo_data
    if not repo_data:
        return None

    labels = [repo['name'] for repo in repo_data]
    stars = [repo['stargazers_count'] for repo in repo_data]
    forks = [repo['forks_count'] for repo in repo_data]
    created_at = [datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ") for repo in repo_data]
    # age = [(datetime.now() - created) for created in created_at]
    age = [(datetime.now() - created).days for created in created_at]

    # Create a DataFrame
    df = pd.DataFrame({
        'name': labels,
        'stars': stars,
        'forks': forks,
        'age': age
    })

    # Create a Plotly bubble chart
    fig = px.scatter(
        df,
        x='forks',
        y='stars',
        size='age',
        hover_data=['name', 'forks', 'stars', 'age'],
        size_max=60  # Adjust the maximum bubble size
    )

    # Customize the chart
    fig.update_layout(
        title='Stars vs. Forks',
        xaxis_title='Number of Forks',
        yaxis_title='Number of Stars',
        hovermode='closest',
        width=800,
        height=600
    )
    response = predict_df(df)
    return st.plotly_chart(fig), st.write(response)
