# personal-finance-advisor- Memu ( Budget Planning , Investment Guidance, Debt Management and Chat with Advisor)

# https://www.investopedia.com/ask/answers/042415/what-is-
# personal-finance-advisor.asp
# https://www.investopedia.com/terms/financialadvisor.asp
# https://www.investopedia.com/personal-finance/
# https://www.investopedia.com/personal-finance-advisor/


# Install python 3.11 
conda create -p venv python==3.11 -y 
# create Python Virtual Environment with python 3.11

conda activate venv/

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