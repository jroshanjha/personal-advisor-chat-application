# [personal-advisor-chat-application](https://github.com/jroshanjha/personal-advisor-chat-application.git)- 

## About this project 
Designed and developed an interactive Personal-advisor-chat-application with features like Learning Platform,  Smart Travel Planner,  Personal Finance Advisor, and a Medical Diagnostic tool. Implemented a user-friendly frontend interface using Streamlit. Integrated the application with Gemini API and Google Services to provide seamless, real-time financial insights and recommendations. 

## Frontend Features Like streamlit with layouts 
Home 
About us 
chat-applications
# Nevigations
 1. "Learning Platform",
 2. "Smart Travel Planner",
 3. "Personal Finance Advisor",
 4. "Medical Diagnostic",
 5. "Logout"

## Learning Platform 
Personalized Lessons -> we add features like what topics you want to learn with level of detail. <br>

Practice Exercises -> We add features like user geneated questions for pracitics which they want to practices.<br>

Question Answering -> PDF Questions Answering Techniques when user upload pdf then ask any questions relative these pdf files. <br>

AI Tutor -> Chat with AI tutor and Store chat in local variable untile user active current session. <br>
Flash Card -> Generated Flash Card For any Specific topics. <br>

Lesson Recommendations -> Enter your complitions topic which you have done then automatically suggest you for next Session. <br>

Progress Tracker -> Analytics your progress tracker which you have already or practices.

## Smart Travel Planner ( Plan Itinerary, Flights & Hotels , Local recommedations , Packing List and Travel Chat )
Plan Itinerary -> Plan your trip with our interactive map and get recommendations for the best places to visit. <br>

Flights & Hotels -> Search Flights and Hotels according Departure {origin} , Designation {destination} and departure date {departure_date} , Return Date <br>

Local recommedations -> Enter your locations then recommended you for your restaurants, and activities.<br>

Packing List -> Generated Packing list accorings your area and locations which kind of item of you needs. <br>

Travel Chat -> You can also chat with its and store in chat history. <br>

## Personal Finance Advisor ( Budget Planning, Investment Guidance , Debt Management & Chat with Advisor)
Budget Planning-> you can take advice about your savings money for your current salary , monty expensive and how many amount you want to save.. <br>

Investment Guidance -> How can you start investment with money  <Br>
Debt Management- > geneated next EMI money according previsous EMI money with interest. <br>
Chat with Advisor ->  <br>

## Medical Diagnostic  ( Symptom Diagnosis , File Summary  , Drug Information & Healthcare Finder )
Symptom Diagnosis -> brief description about the provide a list of possible diagnoses and recommended actions.

File Summary -> provides File summary information and gives relevant tags

Drug Information & Healthcare Finder ...

# https://www.investopedia.com/ask/answers/042415/what-is-
# personal-finance-advisor.asp
# https://www.investopedia.com/terms/financialadvisor.asp
# https://www.investopedia.com/personal-finance/
# https://www.investopedia.com/personal-finance-advisor/


# Install python 3.11 
conda create -p venv python==3.11 -y 
# create Python Virtual Environment with python 3.11

conda activate venv/
venv\Scripts\activate

# installment Requirements Library
pip install -r requirements.txt

# Procfile
streamlit run app.py

# For render.com
web: streamlit run app.py
streamlit run streamlit_app.py --server.port $PORT

# Procfile
web: gunicorn app:app

# requirements.txt
flask
gunicorn

# For Render.com:
# Build command: pip install -r requirements.txt
# Start command: gunicorn app:app

## .env file configuations:-
Creatr .env file and past there...
GOOGLE_API_KEY ="AIzaSyCKnIRMMdFQtgP6C77T3EdmoL9R_wW7m0g"
GOOGLE_API_SERVICE ="AIzaSyCWsS5zmsstSDipuLUHyfVLFP-1LkcVlxs"