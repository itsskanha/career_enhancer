# Career Enhancer App

The Career Enhancer App is a powerful tool designed to boost your professional growth by providing data-driven insights and personalized recommendations. It offers two main features: GitHub Profile Analysis and Project Recommendations.

## Features

### 1. GitHub Profile Analysis

Unlock the full potential of your GitHub profile with our comprehensive analysis tool. By simply entering your GitHub username, our app leverages the GitHub API to fetch your profile data and performs an in-depth analysis using Python's Plotly library.

Key Visualizations:
- Stars vs. Repository Analysis: Compare the popularity of your repositories by number of stars and get llm generated insights from it
- Forks vs. Repository Analysis: Compare the popularity of your repositories by number of forks and get llm generated insights from it
- Language Distribution: See which programming languages you use most
- Stars vs Forks compared by days of repo creation: Compare the popularity of your repositories by number of stars and forks by number of days and get llm generated insights from it
  
This feature helps you understand your GitHub presence better, identify your strengths, and discover areas for improvement. It can also be used by recruiters to screen the github profiles of candidates.

### 2. Project Recommendations

Not sure what to build next? Our Project Recommendation feature has got you covered. It uses advanced language models (LLMs) to suggest tailored project ideas based on your inputs:

- Domain: Computer Science/ Marketing/ Design etc
- Area of Interest: e.g., Web Development, AI/ML, Mobile Apps / Brand Strategy, Brand Expansion / UI/UX Designer, 3d Modelling etc
- Experience Level: Student/ Working professional/ Freelancer
- Years of Experience: Number of years of experience
- Skill level :  Beginner, Intermediate, Advanced
- Tech Stack: Languages and frameworks you're proficient in or want to learn
- Prior Projects: List down the prior projects if you have any
- Hours in Hand: Number of hours you have for one project
- 
The LLM analyzes your preferences and generates project ideas that align with your goals, helping you stay challenged and grow your skills.

#### GitHub Optimization

As part of the Project Recommendations, we also offer a GitHub Optimization feature. Enter your GitHub username, and our app will:

1. Fetch your GitHub data
2. Analyze it in the context of your project goals
3. Provide actionable tips to enhance your GitHub profile, such as:
   - Adding more projects in your area of interest
   - Improving documentation
   - Increasing community engagement
   - Showcasing specific skills

This ensures your GitHub profile accurately reflects your ambitions and attracts the right opportunities.

## Installation

1. Clone the repository:

   git clone https://github.com/itsskanha/career_enhancer.git
   cd career_enhancer

3. Set up a virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

5. Install dependencies:

   pip install -r requirements.txt
   
7. Set up environment variables:

   - If you haven't set up your groqchat api keys, get it on: https://console.groq.com/keys

   - Create a `.env` file in the root directory
   - Add following API keys in the .env file: (We are using two keys to distribute the load)
     - `GROQ_API_KEY=your_key_here`
     - `GROQ_API_KEY_PR=your_another_key_here`
    
9. Run the app:

   streamlit run app.py
   Visit `http://localhost:8501` in your browser to start using the Career Enhancer App.

## Usage

1. GitHub Profile Analysis:
   - Navigate to the "GitHub Analysis" section
   - Type your GitHub username
   - Press Enter

2. Project Recommendations:
   - Go to the "Project Recommendation" section
   - Input your interests, experience, and tech stack
   - Click "Submit" for personalized project ideas
   - (Optional) Enter your GitHub username and click "Optimize GitHub" for profile enhancement tips

## Technologies Used

- Python
- Streamlit (for frontend and hosting)
- Plotly (for data visualization)
- GitHub API
- Language Model API (LLAMA3 via groqchat)

## Contributing

We welcome contributions! Please follow these steps: (I need some more analysis factors for github so if you have any ideas, do let me know)

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Thanks to GitHub for providing the API
- Special thanks to the Plotly team for their excellent visualization library
- Thanks to the Groq team to make the open source models accessible via APIs and their powerful inference engines
- Gratitude to the creators of the Meta-LLAMA3 for powering our recommendation engine

Elevate your career with data-driven insights and tailored guidance. The Career Enhancer App is your partner in professional growth. Start your journey today! 🚀
