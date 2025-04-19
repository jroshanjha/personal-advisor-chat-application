import streamlit as st
from PIL import Image
import database

def home():
    # Page title
    st.title("Home Page")
    st.subheader("Welcome to Personal Advisor AI Chatbot Application!")
    # Call-to-action button
    st.button("Learn More", key="learn_more")
    # Display an image or logo
    st.image("static/images/logo.jfif") # use_column_width=True
    
    # Welcome message
    st.markdown(
        """
        Welcome to the **Home Page** of Personal Advisor AI Chatbot Application. 
        Here, you'll find the latest updates, resources, and insights to get started with Gemini API.
        """
    )
    # Section: Features
    st.header("Features")
    features = [
        "🌟 AI-Powered Learning Platform",
        "📊 Medical Diagnostic Tool",
        "📈 Personal Finance Advisors",
        "🛠️ Smart Travel Planner",
        "🔒 Dynamic data visualizations"
    ]
    for feature in features:
        st.write(feature)
    # Interactive element: Newsletter subscription
    #st.subheader("Subscribe to Our Learning Center")
    st.title("📧 Subscribe to Our Learning Center")
    email = st.text_input("Enter your email address:")
    if st.button("Subscribe"):
        if email:
            if database.insert_email(email):
                st.success(f"Thank you for subscribing, {email}!")
            else:
              st.warning("⚠️ Email already subscribed.")
        else:
            st.error("Please enter a valid email address.")

    # Section: Get started
    st.header("Get Started")
    st.markdown(
        """
        - 👉 **Explore** our Chat app using the sidebar navigation.
        - 📞 **Contact us** for support or feedback.
        """
    )

    # Call-to-action button
    # st.button("Learn More", key="learn_more")

    # Footer section
    st.markdown("---")
    st.markdown("© 2024-2025 Personal Advisor AI Chatbot Application | All rights reserved. Developed by jroshan")

home()