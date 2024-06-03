from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()


def predict_2vars(data_a, data_b, a, b):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""You are a Mentor proficient in GitHub. 

                            Based on github repo data you have to suggest them things,
                            what repo should they contribute more to? Or which language they should do
                            more or where they lack.
                            Give Repo Contribution Suggestions

                            If you see any trends or patterns, do let me know.
                               for example: Trends & Patterns in your github profile:

                            Tell them Strength and Weaknesses of their data
                            Explicitly tell them what job are they suitable for in bullet points based on data
                           """,
            },
            {
                "role": "user",
                "content": f"""These are list of two data in which 
                            {a} : {data_a} and {b} :{data_b}
                            Display the data in a tabular format way
                            Map it as indexes co-relate

                           """
            }
        ],
        max_tokens=2048,
    )
    response = completion.choices[0].message.content
    return response


def predict_df(df):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""You are a Mentor proficient in GitHub.
                            Based on github repo data you have to suggest them things,
                            what repo should they contribute more to?

                            If you see any trends or patterns, do let me know.
                            for example: Trends & Patterns in your github profile:

                            Give Repo Contribution Suggestions
                            Tell them Strength and Weaknesses of their data.
                            Explicitly tell them what job are they suitable for in bullet points based on data
                           """,
            },
            {
                "role": "user",
                "content": f""" This is the list of data {df}
                                In it the columns are repo names, stars, forks, days since repo was created.
                                Display the entire data in a tabular format way
                                If you see any trends or patterns, do let me know.
                                For example: sometimes, a repo with less days is doing good,
                                so you can advise to mae it better so that it does even better 
                                Map it as indexes co-relate.
                                Display the data in a tabular format way
                           """
            }
        ],
        max_tokens=2048,
    )
    response = completion.choices[0].message.content
    return response