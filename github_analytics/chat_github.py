from github_analytics.fetch_data import fetch_user_data
import datetime
from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()


def clean_github_data(user_data, repo_data):
    data = {'name': user_data['login'],
            'followers': user_data['followers'],
            'public_repos': user_data['public_repos'],
            'following': user_data['following']}
    created_at = datetime.datetime.strptime(user_data['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    data['account_age'] = (datetime.datetime.now() - created_at).days // 365

    data['repo_names'] = []
    for repos in repo_data:
        data['repo_names'].append(repos['name'])

    data['size_of_repos'] = []
    for repos in repo_data:
        data['size_of_repos'].append(repos['size'])

    data['languages'] = []
    for repos in repo_data:
        data['languages'].append(repos['language'])

    data['topics'] = []
    for repos in repo_data:
        data['topics'].append(repos['topics'])

    data['no_of_repos'] = len(data['repo_names'])
    data['total_stars'] = sum(repo['stargazers_count'] for repo in repo_data)
    data['total_watchers'] = sum(repo['watchers_count'] for repo in repo_data)
    data['total_open_issues'] = sum(repo['open_issues'] for repo in repo_data)

    data['most_starred_repo'] = max(repo_data, key=lambda x: x['stargazers_count'])['name']
    data['most_watched_repo'] = max(repo_data, key=lambda x: x['watchers_count'])['name']
    data['most_forked_repo'] = max(repo_data, key=lambda x: x['forks_count'])['name']
    return data


# print(clean_github_data(user_data, repo_data))


def analyze_github_data(username, domain, area_of_interest, experience_level,
                        years_of_experience, skill_level, tech_stack, prior_projects,
                        hours_in_hand):
    user_data, repo_data = fetch_user_data(username)
    data = clean_github_data(user_data, repo_data)
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""You are an expert at github and technological aspects. 
                                You are a mentor to one of such people.
                                They come at you with data about their github repositories.

                                They also give data about their domain, area of interest, exprience level,
                                years of experience, skill level, tech stack, prior projects, hours in hand
                                showing where they want to improve

                                Start your answer with , 'Based on your github stats'
                                Clearly mention stats from their github repository which stand out to you

                            """,
            },
            {
                "role": "user",
                "content": f"""You are given the following data {data}. It has 
                            (['name', 'followers', 'public_repos', 'following', 'account_age', 'repo_names',
                                'size_of_repos', 'languages', 'topics', 'no_of_repos', 'total_stars', 'total_watchers',
                                'total_open_issues', 'most_starred_repo', 'most_watched_repo', 'most_forked_repo'])

                            You also know my:

                            Domain: {domain}
                            Area of Interest: {area_of_interest}
                            Experience Level: {experience_level}
                            Years of Experience: {years_of_experience}
                            Skill level : {skill_level}
                            Tech Stack: {tech_stack}
                            Prior Projects: {prior_projects}
                            Hours in Hand: {hours_in_hand}

                            Based on my github stats, you should recommend me what kind of projects
                            I should be doing more and what should be visible more on my github.
                            give tips to enhance my github
                            """,
            }
        ],
        max_tokens=4096,
    )
    response = completion.choices[0].message.content
    return response