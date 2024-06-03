import streamlit as st
from groq import Groq
from github_analytics.chat_github import analyze_github_data

import os
from dotenv import load_dotenv
load_dotenv()


def predict(domain, content):
    client = Groq(api_key=os.getenv("GROQ_API_KEY_PR"))
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""You are a Mentor proficient in the {domain} that provides project recommendations
                           in a rabular format to users based on their domain, area of interest, experience level,
                           years of experience, tech stack, and prior projects.

                           Strictly give the output in a tabular format
                           """,
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        max_tokens=2048,
    )
    response = completion.choices[0].message.content
    return response


def project_recommendation():
    st.title("Project Recommender Chatbot")

    domain = st.text_input("Enter your domain:")
    area_of_interest = st.text_input("Enter your area of interest:")
    experience_level = st.selectbox("Select your current role", ['Student', 'Working professional', 'Freelancer'])

    if experience_level in ["Working professional", "Freelancer"]:
        years_of_experience = st.number_input("Enter your years of experience:")
    else:
        years_of_experience = 0

    skill_level = st.selectbox("Select your skill level", ['Beginner', 'Intermediate', 'Advanced'])
    tech_stack = st.text_input("Enter your technology stack/ list of tools you use for your project:")
    prior_projects = st.text_input("If you have any prior projects, please enter:")
    hours_in_hand = st.number_input("How many hours do you have for one project?")

    content = f"""This is my information:

            Domain: {domain}
            Area of Interest: {area_of_interest}
            Experience Level: {experience_level}
            Years of Experience: {years_of_experience}
            Skill level : {skill_level}
            Tech Stack: {tech_stack}
            Prior Projects: {prior_projects}
            Hours in Hand: {hours_in_hand}

            Based on this information, please provide a list of 5 project recommendations
            that would be suitable for me.
            Consider my domain, area of interest, years of experience, hours in hand, experience level, tech stack,
            skill level, and any prior projects I have worked on.
            Tailor the recommendations to my specific interests and skill level. 
            You have an explicit instruction to follow the hours in hand criteria and
            not overestimate/underestimate the time

            For each project recommendation, provide the following details in a tabular format:

            1. Project Title
            2. Brief Project Description
            3. Relevant Technologies/Skills Required
            4. Steps to achieve the recommendation 

            If it is a technology related domain, in 4th point above,
            please mention the step by step modules/files/subprojects that one can make and progress in a project

            Your response should be structured in a clear and concise manner, do not use </br> anywhere
            with each project recommendation presented as a separate section or bullet point."""

    if st.button("Send"):
        answer = predict(domain, content)
        st.write("Result:", answer)

    st.write("If you are from a technical field and you want to analyze your github, press this button")
    username = st.text_input("Enter your Github Username: ")
    if username:
        # user_data, repo_data = fetch_user_data(username)
        output_of_analysis = analyze_github_data(username, domain, area_of_interest, experience_level,
                                                 years_of_experience, skill_level, tech_stack, prior_projects,
                                                 hours_in_hand)
        st.write("Result:", output_of_analysis)