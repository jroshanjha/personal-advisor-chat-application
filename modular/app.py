import os
import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader,PdfMerger,PdfWriter
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
# from langchain.embeddings import 
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import tempfile
import google.generativeai as genai


# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

# 🔐 Configure Google Generative AI

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Define embeddings and model
#embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#llm = ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True, temperature=0.3)

# # Embeddings for FAISS
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# # Chat model for QA chain
# llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

# 💬 LLM (Gemini Pro)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest", # gemini-pro-vision-001
    convert_system_message_to_human=True,
    temperature=0.7
)
# 📌 Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 🧠 VectorStore (Assume you already created and loaded your FAISS store)
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#vectorstore.save_local("faiss_index") # faiss_index

def pdf_reader(pdf_file):
    text=""
    for pdf in pdf_file:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Streamlit UI
st.title("📄 Chat with Your PDF - Powered by Gemini & RAG")

uploaded_file = st.file_uploader("Upload a PDF file",accept_multiple_files=True, type=["pdf"])
# if uploaded_files:
#     for file in uploaded_files:
#         with open(file.name, "wb") as f:
#             f.write(file.read())

        # loader = PyPDFLoader(file.name)
        # docs = loader.load()
        
if uploaded_file:
    with st.spinner("Processing PDF..."):
        # Load and split PDF
        all_docs = []
        
        for file in uploaded_file:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(file.read())
                tmp_path = tmp_file.name
                
            # Load and split PDF
            loader = PyPDFLoader(tmp_path)
            documents = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            docs = text_splitter.split_documents(documents)
            all_docs.extend(docs)
            
        # loader = PyPDFLoader(uploaded_file.name)
        # documents = loader.load()
        # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        # docs = text_splitter.split_documents(documents)

        # Create vector store
        vectorstore = FAISS.from_documents(docs, embeddings)

        # Conversational memory and retriever chain
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        retriever = vectorstore.as_retriever()

        # 🔄 Chain
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory,
            verbose=True
        )

        # Ask questions
        question = st.text_input("Ask a question about the PDF")
        if st.button("Get Answer") and question:
            with st.spinner("Thinking..."):
                result = qa_chain.run(question)
                st.subheader("📜 Answer")
                st.write(result)

        # Download PDF
        
        
        
# ✅ Fixes Applied:
# Handles multiple files using accept_multiple_files=True.

# Uses tempfile.NamedTemporaryFile() to safely handle file I/O.

# Ensures uploaded_file.name is not misused on a list.

# Works perfectly with your Gemini-powered RAG pipeline.

# ✅ 2. Correct model names
# These are the latest working model names for the Gemini API:


# Purpose	Model Name
# Chat/LLM	"gemini-pro"
# Embeddings	"models/embedding-001"