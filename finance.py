import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
# from .pages import about, home
# from . import travel

# Page options
# PAGES = {
#     "Home": home,
#     "About Us": about,
#     "Travel": travel,
# }

load_dotenv()
## configure the api key:-
genai.configure(api_key=os.getenv("GOOGLE_API_SERVICE"))

# Set up API keys
#OPENAI_API_KEY = "your_openai_api_key"  # Replace with Gemini API key if applicable
#openai.api_key = OPENAI_API_KEY

model = genai.GenerativeModel("learnlm-1.5-pro-experimental")
#model = genai.GenerativeModel("gemini-pro")
#gemini-1.5-pro-001

# # Sidebar navigation
# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# # Load the selected page
# page = PAGES[selection]
# page.app()


f_chat = model.start_chat(history=[])

def get_gemini_response_store(question,k):    
    if k=='f':
        response=f_chat.send_message(question,stream=True)
        return response
def get_gemini_response(text):
    response = model.generate_content(text)
    return response.text
if 'fchat_history' not in st.session_state:
    st.session_state['fchat_history'] = []
def financial():
    #title for title bar:- 
    ##st.set_page_config("Personal Finance Advisor 💰")    
    # Title
    st.title("Welcome to Personal Finance Advisor 💰")
    #st.header("Personal Finance Advisor:-💁")
    # Sidebar Menu
    menu = st.sidebar.radio("Menu", ["Budget Planning", "Investment Guidance", "Debt Management", "Chat with Advisor"])
    prompt = "Tell me about Financial Advisor"
    if menu == "Budget Planning":
        st.header("Budget Planning ")
        income = st.number_input("Enter your monthly income", min_value=0)
        expenses = st.number_input("Enter your monthly expenses", min_value=0)
        savings_goal = st.number_input("Enter your savings goal", min_value=0)

        if st.button("Get Suggestions"):
            prompt = f"My monthly income is {income}, expenses are {expenses}, and my savings goal is {savings_goal}. Suggest ways to optimize my budget."
            st.write("----------------------------------------------------------------")
            st.write(f"Your Monthly income is {income}, expenses are {expenses}, and savings goal is {savings_goal}. Suggest ways to optimize your budget")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
            
    elif menu == "Investment Guidance":
        st.header("Investment Guidance😃")
        risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
        time_frame = st.slider("Investment Time Frame (Years)", 1, 30, 5)
        goal = st.text_input("Investment Goal")
        if st.button("Get Investment Advice"):
            prompt = f"I have a {risk}-risk tolerance, a {time_frame}-year investment horizon, and my goal is {goal}. Suggest investment strategies."
            st.write("----------------------------------------------------------------")
            st.write(f"Suggest investment strategies : your {risk}-risk tolerance, a {time_frame}-year investment , and your goal is {goal}. ")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
            
    elif menu == "Debt Management":
        st.header("Debt Management💡")
        debt = st.number_input("Total Debt Amount", min_value=0)
        interest_rate = st.number_input("Interest Rate (%)", min_value=0.0)
        monthly_payment = st.number_input("Monthly Payment", min_value=0)

        if st.button("Get Repayment Plan"):
            prompt = f"My total debt is {debt} with an interest rate of {interest_rate}%, and I can pay {monthly_payment} monthly. Suggest a repayment plan."
            st.write("----------------------------------------------------------------")
            st.write(f"Debt Management: {debt} with interest rate of {interest_rate}%, and paying {monthly_payment} monthly Amount")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
            
    elif menu == "Chat with Advisor":
        st.header("Chat with Your Financial Advisor🧑")
        user_query = st.text_input("Ask a question")
        if st.button("Submit"):
            prompt = user_query
            st.write("----------------------------------------------------------------")
            st.write(f"### Financial's Answer: for {user_query} :-")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response_store(prompt,'f')
            # response = openai.Completion.create(
            #     engine="text-davinci-003", prompt=user_query, max_tokens=150
            # )
            # st.write(response['choices'][0]['text'])
            st.session_state['fchat_history'].append(("You", user_query))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['fchat_history'].append(("Bot", chunk.text))
        st.subheader("The Chat History is")
        for role, text in st.session_state['fchat_history']:
            st.write(f"{role}: {text}") 
   
# # Main
if __name__ == "__main__":
    financial()