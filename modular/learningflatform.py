from datetime import date
import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image
# from sklearn.linear_model import LinearRegression 

# Store and index data in multi dimensional vectors.
# Chroma , milves, Pipecone , Faiss 


# for pdf reader or writer
from PyPDF2 import PdfReader,PdfMerger,PdfWriter
# for pdf text splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter 
# words embedding means convert into word vectorized 
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
# from langchain.llms import GoogleGenerativeAI
#from langchain.vectorstores import FAISS 

# New Import
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain 
from langchain.prompts import PromptTemplate


load_dotenv()
## configure the api key:-
genai.configure(api_key=os.getenv("GOOGLE_API_SERVICE"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")
#model = ChatGoogleGenerativeAI(model="gemini-pro")

l_chat = model.start_chat(history=[])
lr_chat = model.start_chat(history=[])
def get_gemini_response_store(question,k):    
    if k=='l':
        response=l_chat.send_message(question,stream=True)
    if k =='lr':
        response=lr_chat.send_message(question,stream=True)
    return response
# MySQL Connection Configuration :- begin configuration:-
# db_config = {
#     "host": "localhost",
#     "user": "root",  # Replace with your MySQL username
#     "password": "jroshan@98",  # Replace with your MySQL password
#     "database": "learning_model"  # Replace with your MySQL database name
# }
# connect Mysql:-
def get_db_conn():
    #return mysql.connector.connect(**db_config)
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="jroshan@98",
        database="learning_model",
        port =3306
    )
def get_gemini_response(text):
    response = model.generate_content(text)
    return response.text
def log_progress(user_id, lesson_name, score):
    conn = get_db_conn()
    cursor = conn.cursor()
    try:
        #cursor.execute("use learning_model")
        cursor.execute("""
            INSERT INTO progress (user_id, lesson_name, score)
            VALUES (%s, %s, %s)
        """, (user_id, lesson_name, score))
        conn.commit()
        st.success("User Log Progress successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
        # return True

def fetch_user_progress(user_id):
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="jroshan@98",
    #     database="learning_model"
    # )
    # cursor = conn.cursor()
    conn = get_db_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT lesson_name,score,timestamp
            FROM progress
            WHERE user_id = %s
            ORDER BY timestamp DESC
        """, (user_id,))
         # timestamp, max(score) as maximum,min(score) as minimum,avg(score) as average,sum(score) as total_score,count(score) as total
         # group by lesson_name,timestamp
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()    
        conn.close()
    #return pd.DataFrame(rows, columns=["Lesson","Timestamp","Maximum","Minimum","Average","Total Score","Total"])
    dataframe = pd.DataFrame(rows, columns=["Lesson", "Score", "Timestamp"])
    #dataframe['fixed_length'] = dataframe['Lesson'].astype(str).str.slice(0, 50)
    #dataframe['fixed_length'] = dataframe['Lesson'].apply(lambda x: str(x)[:50] if pd.notnull(x) else x)
    # Truncate paragraph to 50 characters
    # ✅ For each row: truncate if longer than 50 chars
    dataframe['fixed_length'] = dataframe['Lesson'].apply(
        lambda x: x[:50] if isinstance(x, str) and len(x) > 50 else x
    )

    dataframe['fixed_size'] = dataframe['Lesson'].str.len()
    dataframe['fixed_size'] = dataframe['fixed_size'].astype(float)
    return dataframe

def plot_progress(dataframe):
    # Create a figure with 2 rows and 3 columns
    #fig, axes = plt.subplots(5, 1, figsize=(30, 30))  # 5 rows, 1 columns
    
    dataframe = dataframe.groupby(['fixed_length','fixed_size'])['Score'].max().reset_index()[['fixed_length','Score','fixed_size']]
    #dataframe['Score'] = dataframe['Score'].astype(int)
    
    # Lesson length fixed:-
    #dataframe = dataframe[dataframe['Lesson'].str.len() <= 50][['Lesson','Score']]
    dataframe = dataframe.sort_values('Score', ascending=False)
    
    #return dataframe

    # Line Plot
    fig1 = plt.figure(figsize=(15, 5))
    plt.plot(dataframe["fixed_length"], dataframe["Score"], marker="o", color="b")
    plt.title("Line Plot - User Progress")
    plt.xlabel("Lesson")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Bar Chart
    fig2 = plt.figure(figsize=(15, 5))
    plt.bar(dataframe["fixed_length"], dataframe["Score"], color="skyblue")
    plt.title("Bar Chart - User Progress")
    plt.xlabel("Lesson")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Histogram
    fig3 = plt.figure(figsize=(30, 5))
    plt.hist(dataframe["fixed_length"], bins=5, color="orange", edgecolor="black")
    plt.title("Histogram - Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    st.pyplot(fig3)

    # Pie Chart
    fig4 = plt.figure(figsize=(25, 5))
    plt.pie(
        dataframe["Score"], 
        labels=dataframe["fixed_length"], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired.colors
    )
    plt.title("Pie Chart - Score Distribution")
    st.pyplot(fig4)
    
    # Scatter Plot
    fig5 = plt.figure(figsize=(15, 5))
    plt.scatter(dataframe["fixed_length"], dataframe["Score"], color="green", alpha=0.7)
    plt.title("Scatter Plot - User Progress")
    plt.xlabel("Lesson")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    st.pyplot(fig5)

    # Correlation Heatmap
    fig6 = plt.figure(figsize=(10, 5))
    plt.title("Correlation Heatmap - User Progress")
    sns.heatmap(dataframe[['Score','fixed_size']].corr(), annot=True, cmap="coolwarm")
    st.pyplot(fig6)
    
    # Box plot 
    fig7 = plt.figure(figsize=(10, 5))
    sns.boxplot(dataframe["Score"])
    plt.title("Box Plot - User Progress")
    st.pyplot(fig7)
    
    # Violin plot 
    fig8 = plt.figure(figsize=(10, 5))
    sns.violinplot(dataframe["Score"])
    plt.title("Violin Plot - User Progress")
    st.pyplot(fig8)
    
    # KDE plot
    fig9 = plt.figure(figsize=(10, 5))
    sns.kdeplot(dataframe["Score"], fill=True, shade=True)
    plt.title("KDE Plot - User Progress")
    st.pyplot(fig9)
    
    # Heatmap
    fig10 = plt.figure(figsize=(10, 5))
    sns.heatmap(dataframe[['Score','fixed_size']].corr(), annot=True, cmap="coolwarm")
    plt.title("Heatmap - User Progress")
    st.pyplot(fig10)
    
    # Swarm plot
    fig11 = plt.figure(figsize=(10, 5))
    sns.swarmplot(dataframe["Score"])
    plt.title("Swarm Plot - User Progress")
    st.pyplot(fig11)

    # lmplot 
    dataframe['Lesson_ID'] = dataframe.index  # or use LabelEncoder if needed
    # fig5 = plt.figure(figsize=(10, 5))
    # sns.lmplot(x="Lesson_ID", y="Score",data = dataframe)
    # plt.title("LM Plot - User Progress")
    # plt.xlabel("Lesson")
    # plt.ylabel("Score")
    # plt.xticks(rotation=45)
    # st.pyplot(fig5)
    # Create a numeric version of the fixed_length column
    dataframe['fixed_length_num'] = dataframe['fixed_length'].apply(lambda x: len(x) if isinstance(x, str) else 0)
    
    fig5 = plt.figure(figsize=(10, 5))
    sns.regplot(x="fixed_length_num", y="Score", data=dataframe)
    plt.title("LM Plot - User Progress")
    plt.xlabel("Lesson Length")
    plt.ylabel("Score")
    st.pyplot(fig5)
    
    # Linear Regression
    # X = dataframe["fixed_length"].values.reshape(-1, 1)
    # y = dataframe["Score"].values.reshape(-1, 1)
    # model = LinearRegression().fit(X, y)
    # y_pred = model.predict(X)
    # plt.scatter(dataframe["fixed_length"], dataframe["Score"], color="green", alpha=0.7)
    # plt.plot(dataframe["fixed_length"], y_pred, color="red", linewidth=2)
    # plt.title("Linear Regression - User Progress")
    # plt.xlabel("Lesson")
    # plt.ylabel("Score")
    # plt.xticks(rotation=45)
    # st.pyplot(plt)
    
    # fig6 = sns.lmplot(x="fixed_length", y="Score", data=dataframe, aspect=2)
    # st.pyplot(fig6)
    
def pdf_reader(pdf_file):
    text=""
    for pdf in pdf_file:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Chunck PDF 
def chunk_pdf(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    chunk_split = splitter.split_text(text)
    return chunk_split

# Get Vectors functions
def get_vectors(text):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectors_store = FAISS.from_texts(text,embedding=embeddings)
    vectors_store.save_local("faiss_index") # faiss_index
    
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    # gemini-1.5-pro / gemini-pro / gemini-1.5-pro-latest / gemini-1.5-pro-001
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embedding_model = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    #embeddings = GoogleGenerativeAIEmbeddings(model="embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embedding_model,
                             allow_dangerous_deserialization=True  # Enable this only if you trust the source
    )
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=False)
    
    print(response)
    st.write("Reply: ", response["output_text"])
    
# Initialize session state for chat history if it doesn't exist
if 'lchat_history' not in st.session_state:
    st.session_state['lchat_history'] = []
    
if 'lrchat_history' not in st.session_state:
    st.session_state['lrchat_history'] = []
    
def dashboard():
    #st.set_page_config("AI-Powered Learning Platform 📚")
    # App Title
    st.title("Welcome to AI-Powered Learning Platform 📚")
    # Sidebar Menu
    menu = st.sidebar.radio("Menu", ["Personalized Lessons","Practice Exercises", "Question Answering","Image Analyzer","AI Tutor","Flash Card" ,"Lesson Recommendations","Progress Tracker"])
    prompt = "Tell me about Learning Platform"
    if menu == "Personalized Lessons":
        st.header("Generate Personalized Lessons")
        subject = st.text_input("Enter Subject (e.g., Python, Calculus, Machine Learning , Deep Learning,NLP , SQL , Data Science)")
        level = st.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
        goal = st.text_area("What would you like to learn?")
        if st.button("Generate Lesson"):
            prompt = f"Create a detailed lesson on {subject} at a {level} level. Learning goal: {goal}."
            st.write("----------------------------------------------------------------")
            st.write(f"### Lesson Content: for {subject} , {level} and {goal} :-")
            st.write("----------------------------------------------------------------")
            random_number = np.random.randint(40,100)
            result = log_progress(st.session_state.username,subject,random_number) # 88
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
            
    elif menu == "Practice Exercises":
        st.header("Practice Exercises")
        topic = st.text_input("Enter Topic (e.g., Python, Stastics,Hypothesis Testing Machine Learning , Deep Learning,NLP , SQL , Data Science)")
        num_questions = st.slider("Number of Questions", 1, 100, 5)
        if st.button("Generate Exercises"):
            random_number = np.random.randint(60,100)
            result = log_progress(st.session_state.username,topic,random_number) # 88
            prompt = f"Create {num_questions} practice questions with answers on {topic}."
            st.write("----------------------------------------------------------------")
            st.write(f"### Practice Questions: for {topic} :-")
            st.write("----------------------------------------------------------------")
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
        
    elif menu == "AI Tutor":
        st.header("Chat with the AI Tutor")
        question = st.text_input("Ask a question about any topic (e.g., 'Explain Machine Learning or NLP')")
        if st.button("Get Answer"):
            prompt = f"Explaine this topic {question} in depth for interview and exam pointviews."
            st.write("----------------------------------------------------------------")
            st.write(f"### Tutor's Answer: for {question} :-")
            st.write("----------------------------------------------------------------")
            # random_number = np.random.randint(30,100)
            # result = log_progress(st.session_state.username,prompt,random_number)
            response = get_gemini_response_store(prompt,'l')
            #st.write(response)
            # Add user query and response to session state chat history
            st.session_state['lchat_history'].append(("You", question))
            st.session_state['lchat_history'].append(("----------------------------------------", ""))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['lchat_history'].append(("Bot", chunk.text))
            st.session_state['lchat_history'].append(("---------------Thank you for using AI Tutor!-------------------------", ""))    
        # Show chat history
        st.subheader("The Chat History is")
        for role, text in st.session_state['lchat_history']:
            st.write(f"{role}: {text}")   
            
    elif menu =='Flash Card':
        topic = st.text_input("Enter Topic for Flashcards")
        if st.button("Generate Flashcards"):
            prompt = f"Create top 100 flashcards with questions and answers on {topic}."
            st.write("----------------------------------------------------------------")
            st.write(f"# Top 100 Flashcards Questions and Answers: for Topics:- {topic} :-")
            st.write("----------------------------------------------------------------")
            random_number = np.random.randint(40,100)
            result = log_progress(st.session_state.username,topic,random_number)
            response = get_gemini_response(prompt)
            st.subheader('The response Output:-')
            st.write(response)
    elif menu=='Lesson Recommendations':
        c_lesson = st.text_input("Enter Your Complete Topics")
        if st.button("Recommendations Next Lesson!"):
            prompt = f"I have Completes the lesson {c_lesson} and pleased Recommendations Next Lesson or Topic!"
            st.write("----------------------------------------------------------------")
            st.write(f'Recommedations Next Lesson and Topics: for {c_lesson} :-')
            st.write("----------------------------------------------------------------")
            response = get_gemini_response_store(prompt,'lr')
            
            st.session_state['lrchat_history'].append(("You", c_lesson))
            st.session_state['lrchat_history'].append(("--------------------------------------------------------",""))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['lrchat_history'].append(("Bot", chunk.text))
            st.session_state['lrchat_history'].append(("--------------------Thank you for using AI Tutor!---------------------",""))
        st.subheader("The Chat History is")
        for role, text in st.session_state['lrchat_history']:
            st.write(f"{role}: {text}")
            # response = get_gemini_response(prompt)
            # st.subheader('The response Output:-')
            # st.write(response)
    elif menu=='Question Answering':
        st.header("Chat with PDF File")
        pdf_file = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True,type=["pdf"]) # True
        if st.button("Submit & Process"):
            if pdf_file:
                with st.spinner("Processing..."):
                    raw_text = pdf_reader(pdf_file)
                    chunk_text = chunk_pdf(raw_text)
                    get_vectors(chunk_text)
                    st.success("Done")
            else:
                st.error("Please upload a PDF file")
        st.write("----------------------------------------------------------------")        
        user_question = st.text_input("Ask a Question from the PDF Files")
        st.write("----------------------------------------------------------------")
        if user_question:
            user_input(user_question)
    elif menu =="Image Analyzer":
        # Streamlit UI
        st.title("🧠 Gemini Image Analyzer")
        st.markdown("Upload an image and Gemini will describe it or answer questions about it!")
        
        # Upload image
        uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])
        
        # Text prompt (optional)
        prompt = st.text_input("🔍 What do you want Gemini to tell you about this image?", value="Describe this image in detail")
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image") # use_column_width=True

            if st.button("Analyze Image"):
                with st.spinner("Analyzing..."):
                    # Convert image to bytes
                    image_bytes = uploaded_file.getvalue()

                    # Gemini Vision model input
                    response = model.generate_content([
                        prompt,
                        {
                            "mime_type": "image/png",
                            "data": image_bytes
                        }
                    ])

                    # Output result
                    st.subheader("🧾 Gemini's Analysis:")
                    st.write(response.text)

    elif menu == "Progress Tracker":
        st.header("Track Your Progress")
        user_id = st.text_input("Enter User ID", st.session_state.username)
        #st.write("Feature Coming Soon: Integrate with user authentication and database to track completed lessons, scores, and improvement areas.")
        if st.button("View Progress"):
            progress_df = fetch_user_progress(user_id)
            if not progress_df.empty:
                st.write("----------------------------------------------------------------")
                st.subheader("### Progress Data:")
                st.write("----------------------------------------------------------------")
                st.dataframe(progress_df)
                plot_progress(progress_df)
            else:
                st.write("No progress data found!")

# Main
# if __name__ == "__main__":
#     dashboard()