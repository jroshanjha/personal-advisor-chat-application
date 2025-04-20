from datetime import date
import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
# from langchain.embeddings import GoogleGenerativeAIEmbeddings

load_dotenv()
## configure the api key:-
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro-001")
#model = ChatGoogleGenerativeAI(model="gemini-pro")

# model = ChatGoogleGenerativeAI(
#     model="gemini-pro",
#     temperature=0.3,
#     convert_system_message_to_human=True
# )

embedding = GoogleGenerativeAIEmbeddings(model="embedding-001")

#t_chat = model.start_chat(history=[])
# r_chat = model.start_chat(history=[])

# Initialize chat and history in session state
if 't_chat' not in st.session_state:
    st.session_state.t_chat = model.start_chat(history=[])
    
if 'tchat_history' not in st.session_state:
    st.session_state.tchat_history = []
    
if 'r_chat' not in st.session_state:
    st.session_state.r_chat = model.start_chat(history=[])
    
if 'rchat_history' not in st.session_state:
    st.session_state.rchat_history = []
    
def get_gemini_response(text):
    response = model.generate_content(text)
    return response.text
def get_gemini_response_store(question,k):
    if k=='t':
        #response=t_chat.send_message(question,stream=True)
        response = st.session_state.t_chat.send_message(question, stream=True)
    if k =='r':
        response = st.session_state.r_chat.send_message(question, stream=True)
    return response

# Stream response from Gemini
#response_stream = st.session_state.gemini_chat.send_message(user_input, stream=True)
    
# if 'tchat_history' not in st.session_state:
#     st.session_state['tchat_history'] = []
    
def t_ravel():
    ##title for title bar:- 
    ##st.set_page_config("Smart Travel Planner 🌍")  
    # Page title
    st.title("Welcome to Smart Travel Planner 🌍")
    # Sidebar Menu
    menu = st.sidebar.radio("Menu", ["Plan Itinerary", "Flights & Hotels", "Local Recommendations", "Packing List", "Travel Chat"])
    prompt = "Tell me about Travel Planner"
    if menu == "Plan Itinerary":
        st.header("Plan Your Itinerary")
        destination = st.text_input("Enter Destination")
        start_date = st.date_input("Start Date", min_value=date.today())
        end_date = st.date_input("End Date", min_value=start_date)
        preferences = st.text_area("Enter Your Preferences (e.g., museums, beaches, nightlife)")

        if st.button("Generate Itinerary"):
            prompt = f"Plan a detailed trip itinerary for {destination} from {start_date} to {end_date}. Preferences: {preferences}."
            st.write("----------------------------------------------------------------")
            st.write(f"Generate Itinerary plan for {destination} from {start_date} to {end_date}. Preferences: {preferences}.")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)

    elif menu == "Flights & Hotels":
        st.header("Find Flights and Hotels")
        origin = st.text_input("Departure City")
        destination = st.text_input("Destination City")
        departure_date = st.date_input("Departure Date", min_value=date.today())
        return_date = st.date_input("Return Date", min_value=departure_date)

        if st.button("Search Deals"):
            prompt = f"Search Flights and Hotels for Departure {origin} , Designation {destination} and departure date {departure_date} , Return Date {return_date} "
            #st.write("Fetching deals... (Integrate with Skyscanner or Expedia API here)")
            st.write("----------------------------------------------------------------")
            st.write(f"Flights & Hotels Services: for details departure city {origin} and Destination city {destination} and Departure Date{departure_date} and Return Date{return_date}")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
            
    elif menu == "Local Recommendations":
        st.header("Discover Local Attractions")
        location = st.text_input("Enter Location")
        if st.button("Get Recommendations"):
            prompt = f"Suggest top attractions, restaurants, and activities in {location}."
            st.write("----------------------------------------------------------------")
            st.write(f"Discover Local Attractions in {location}.")
            st.write("----------------------------------------------------------------")
            #response = get_gemini_response(prompt)
            response = get_gemini_response_store(prompt,'r')
            #st.subheader('The response Output:-')
            #st.write(response)
            question = prompt
            #st.session_state['tchat_history'].append(("You", question))
            st.session_state.rchat_history.append(("You", question))
            st.session_state.rchat_history.append(("----------------------------------------------------------------", "")) # Fetching deals... (Integrate with Skyscanner or Expedia API here)
            
            st.subheader("The Response is")
            full_response = ""
            for chunk in response:
                full_response += chunk.text
                st.write(chunk.text)
            st.session_state.rchat_history.append(("Bot", full_response))
            st.session_state.rchat_history.append(("-----------------------This is the end of the response-------------------------", ""))
            # for chunk in response:
            #     st.write(chunk.text)
            #     st.session_state['tchat_history'].append(("Bot", chunk.text))
                
        # st.subheader("The Chat History is")
        # for role, text in st.session_state['tchat_history']:
        #     st.write(f"{role}: {text}")
            
        # Display full chat history
        st.subheader("🕘 The Chat History is")
        for role, message in st.session_state.rchat_history:
            st.markdown(f"**{role}:** {message}")
            
    elif menu == "Packing List":
        st.header("Packing List Generator")
        destination = st.text_input("Destination")
        travel_dates = st.date_input("Travel Dates", [])  # min_value=date.today()
        activity_type = st.text_area("Activities (e.g., hiking, formal events)")

        if st.button("Generate Packing List"):
            prompt = f"Create a packing list for a trip to {destination}. Dates: {travel_dates}. Activities: {activity_type}."
            st.write("----------------------------------------------------------------")
            st.write(f"Packing List for {destination} from {travel_dates}. Activities: {activity_type}.")
            st.write("----------------------------------------------------------------")
            
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
            
    elif menu == "Travel Chat":
        st.header("Ask Your Travel Assistant")
        question = st.text_input("Ask a question about your trip")
        if st.button("Get Answer"):
            prompt = question
            st.write("----------------------------------------------------------------")
            st.write(f"Chat System response: for {question} :-")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response_store(prompt,'t')
            # response = openai.Completion.create(
            #     engine="text-davinci-003", prompt=question, max_tokens=150
            # )
            # st.write(response['choices'][0]['text'])
            st.session_state['tchat_history'].append(("You", question))
            st.session_state['tchat_history'].append(("----------------------------------------------------------------", ""))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['tchat_history'].append(("Bot", chunk.text))
            st.session_state['tchat_history'].append(("-----------------------This is the end of the response-------------------------", ""))
                
        st.subheader("🕘 The Chat History is")
        for role, text in st.session_state['tchat_history']:
            st.write(f"{role}: {text}") 
                    
            # response = get_gemini_response(prompt)
            # st.subheader('The response Output:-')
            # st.write(response)
# Main
# if __name__ == "__main__":
#     t_ravel()



