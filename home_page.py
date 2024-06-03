import streamlit as st


# Set page configuration
def home_page():
    # Add title and header
    st.title("Career Enhancer")
    st.header("Boost Your Professional Journey")

    # Welcome/Introduction Section
    st.write("""
    Welcome to Career Enhancer, an application designed to help you enhance your development skills and career prospects. We offer three powerful features:

    - **GitHub Analytics**: Gain valuable insights into your GitHub profile and repositories.
    - **Custom Project Recommendation**: Get personalized project recommendations based on your interests and skills.
    """)

    # Feature Highlights
    st.subheader("Feature Highlights")

    # GitHub Analytics
    st.write("### GitHub Analytics")
    st.write("""
    Unlock the power of your GitHub profile with our GitHub Analytics feature.
    Gain valuable insights into your repositories, including:

    - Number of forks and stars
    - Programming language usage
    - Tips and tricks to enhance your GitHub profile
    - And more!

    With this information, you can identify areas for improvement
    and optimize your GitHub presence for better
    visibility and career opportunities.
    """)

    # Custom Project Recommendation
    st.write("### Custom Project Recommendation")
    st.write("""
    - Struggling to find the right project?
    - Provide your area of interest, experience level, and tech stack.
    - Get personalized project suggestions.
    - Analyze your GitHub for useful tips based on your goals.
    - Enhance skills, build a portfolio, and stay ahead with personalized recommendations.
    """)

    # Footer (Optional)
    st.write("---")
    st.write("© 2024 Career Enhancer. All rights reserved.")

