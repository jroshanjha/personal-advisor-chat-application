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
        "💡 Innovation": "We embrace creativity and strive for continuous improvement.",
        "👥 Collaboration": "We believe in teamwork and open communication.",
        "📈 Excellence": "We deliver top-notch solutions with quality in mind.",
        "🌱 Sustainability": "We care about the environment and sustainable practices.",
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
        - **2018**: Founded with a mission to innovate.
        - **2019**: Launched our first successful product.
        - **2021**: Expanded globally with 10k+ users.
        - **2024**: Introducing cutting-edge analytics tools.
        """
    )

    # Interactive FAQ
    st.header("Frequently Asked Questions (FAQ)")
    faq = {
        "What services do you offer?": "We provide data visualization, analytics, and dashboarding solutions.",
        "How can I contact you?": "Visit our Contact page for details.",
        "Are your tools free to use?": "We offer both free and premium plans.",
    }
    for question, answer in faq.items():
        with st.expander(question):
            st.write(answer)

#about()
    # Footer section
    st.markdown("---")
    st.markdown("© 2024 My Chat Application | All rights reserved. Develop by jroshan")
    
about()