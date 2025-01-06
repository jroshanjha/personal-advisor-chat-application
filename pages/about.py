import streamlit as st
from PIL import Image

def about():
    # Page title
    st.title("About Us")
    st.subheader("Who We Are")

    # Display team image
    st.image("static/images/teamwork.jpg", caption="Our Team") # use_column_width=True

    # Mission statement
    st.markdown(
        """
        Welcome to the **About Us** section! We are a team of passionate individuals dedicated to delivering the best solutions for your needs.
        Our mission is to make data accessible, interactive, and actionable for everyone.
        """
    )

    # Core values
    st.header("Our Core Values")
    core_values = {
        "💡 EDA": " How to Python - Numpy, Pandas , Matplotlib and Seaborn are used to Perform EDA operations.",
        "👥 Machine Leraning ": "Find Trend and Pattern for better future Business Decisions.",
        "📈 NLP": "When I have Textual Data Then I go with NLP for Sentiment Analysis , Topic Modeling and Questions & Answering.",
        "🌱 Deep Learning": "When I have Image or Vidoe or Even Huge amout of text data then go with Deep Learning technique( ANN, RNN and CNN ) .",
    }
    for key, value in core_values.items():
        st.markdown(f"**{key}**: {value}")

    # Team section with columns
    st.header("Meet Our Team")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("static/images/members.jfif", caption="Alice - CEO")
        st.markdown("Visionary leader with 10+ years in the industry.")

    with col2:
        st.image("static/images/members2.jfif", caption="Bob - CTO")
        st.markdown("Tech enthusiast and expert in AI solutions.")

    with col3:
        st.image("static/images/members3.jfif", caption="Charlie - COO")
        st.markdown("Operational guru focused on efficiency.")

    # Company history or timeline
    st.header("Our Journey")
    st.markdown(
        """
        - **2018**: Take Admission in BCA ( Bachelor of Computer Application) Ignou.
        - **2022**: Launched our Own Education Insitute.
        - **2022**: Join XYZ Company As Software Developer Internships.
        - **2023**: Join XYZ Company As Software Developer full time jobs.
        - **2025**: Decided to Start or Swith my career in Data Science Domain.
        """
    )

    # Interactive FAQ
    st.header("Frequently Asked Questions (FAQ)")
    faq = {
        "What services do you offer?": "We provide data visualization, analytics, and dashboarding solutions & Machine learning techniques, NLP techniques ,Generative AI.",
        "How can I contact you?": "Visit our Contact page for details.",
        "Are your tools free to use?": "We offer both free and premium plans.( just only Registered & Login)",
    }
    for question, answer in faq.items():
        with st.expander(question):
            st.write(answer)

#about()
    # Footer section
    st.markdown("---")
    st.markdown("© 2024-2025 Personal Advisor Chat Application | All rights reserved. Developed by jroshan")
    
about()