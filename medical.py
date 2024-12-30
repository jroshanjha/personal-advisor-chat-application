from datetime import date
import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
import mysql.connector
import matplotlib.pyplot as plt

load_dotenv()
## configure the api key:-
genai.configure(api_key=os.getenv("GOOGLE_API_SERVICE"))
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(text):
    response = model.generate_content(text)
    return response.text
   
def fetch_drug_info(drug_name):
    url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Drug not found"}
 
def fetch_healthcare_providers(location, specialization):
    api_key = "your_google_api_key"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={specialization}+in+{location}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "No providers found"}
    
def medical_method():
    # Title
    #st.set_page_config("AI-Powered Medical Diagnostic Tool 🩺")
    st.title("Welcome to Medical Diagnostic Tool 🩺")

    # Sidebar Menu
    menu = st.sidebar.radio("Menu", ["Symptom Diagnosis", "Drug Information", "Healthcare Finder"])
    prompt = "Tell me about Medical Diagnostic Tool"
    if menu == "Symptom Diagnosis":
        st.header("Symptom Diagnosis")
        symptoms = st.text_area("Enter your symptoms (e.g., fever, headache, fatigue)")
        
        if st.button("Get Diagnosis"):
            prompt = f"Given the symptoms: {symptoms}, provide a list of possible diagnoses and recommended actions."
            st.write("**Possible Diagnoses and Recommendations:**")

    elif menu == "Drug Information":
        st.header("Drug Information")
        drug_name = st.text_input("Enter the drug name")
        
        if st.button("Search Drug Info"):
            if drug_name:  # Ensure a drug name is entered
                #data = fetch_drug_info(drug_name)
                prompt = f"Give me depth idea about Grug Information:- {drug_name}"
                # if "error" not in data:  # Check for errors in the API response
                #     st.write("**Drug Information:**")
                #     prompt = st.json(data)  # Display the drug data in JSON format
                # else:
                #     st.error(data.get("error", "Unable to fetch drug information."))
                st.write("**Drug Information:**")
                # prompt = st.json(data)
                #st.write("Fetching drug information... (Replace this with an API call to OpenFDA)")
                # Example: Use OpenFDA API for real-time drug data
            else:
                st.warning("Please enter a drug name.")
        
    elif menu == "Healthcare Finder":
        st.header("Find Healthcare Providers")
        location = st.text_input("Enter your location")
        specialization = st.text_input("Enter specialization (e.g., cardiology, dermatology)")
        
        if st.button("Search Providers"):
            providers = fetch_healthcare_providers(location, specialization)
            prompt = f"Search My Health Care Findre for Locations:-{location} and specialication:- {specialization}"
            st.write("** Health Care Information:**")
            # for provider in providers.get("results", []):
            #     st.write(f"Name: {provider['name']}")
            #     st.write(f"Address: {provider['formatted_address']}")
            #     st.write("---")
        
            #st.write("Fetching healthcare providers... (Integrate with Zocdoc or similar API)")
            # Placeholder: Implement Zocdoc or similar API integration
    
    response = get_gemini_response(prompt)
    #st.subheader('The response Output:-')
    st.write(response)
    
# Main
if __name__ == "__main__":
    medical_method()