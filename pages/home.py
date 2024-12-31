import streamlit as st
from PIL import Image

def index():
    # Page title
    st.title("Home Page")
    st.subheader("Welcome to My Chat Boart Application!")
    # Call-to-action button
    st.button("Learn More", key="learn_more")
    # Display an image or logo
    st.image("static/images/logo.jfif") # use_column_width=True

    # Welcome message
    st.markdown(
        """
        Welcome to the **Home Page** of our app. 
        Here, you'll find the latest updates, resources, and insights to get started.
        """
    )

    # Section: Features
    st.header("Features")
    features = [
        "🌟 Easy-to-use interface",
        "📊 Dynamic data visualizations",
        "📈 Real-time analytics",
        "🛠️ Customizable components",
        "🔒 Secure and reliable"
    ]
    for feature in features:
        st.write(feature)

    # Interactive element: Newsletter subscription
    st.subheader("Subscribe to Our Newsletter")
    email = st.text_input("Enter your email address:")
    if st.button("Subscribe"):
        if email:
            st.success(f"Thank you for subscribing, {email}!")
        else:
            st.error("Please enter a valid email address.")

    # Section: Get started
    st.header("Get Started")
    st.markdown(
        """
        - 👉 **Explore** our app using the sidebar navigation.
        - 📞 **Contact us** for support or feedback.
        """
    )

    # Call-to-action button
    st.button("Learn More", key="learn_more")

    # Footer section
    st.markdown("---")
    st.markdown("© 2024 My Chat Application | All rights reserved. Develop by jroshan")

index()