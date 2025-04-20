import streamlit as st
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch

# def main():
#     st.title("NLP Sentiment Analysis & NER App")
#     st.write("Enter text below to analyze its sentiment and extract named entities using pre-trained Hugging Face models.")
#     # User input
#     user_input = st.text_area("Enter text:")
#     if st.button("Analyze Sentiment"):
#         if user_input:
#             sentiment_pipeline = pipeline("sentiment-analysis")
#             result = sentiment_pipeline(user_input)

#             label = result[0]['label']
#             score = result[0]['score']

#             st.write(f"**Sentiment:** {label}")
#             st.write(f"**Confidence Score:** {score:.4f}")
#         else:
#             st.warning("Please enter some text before analyzing.")

#     if st.button("Extract Named Entities"):
#         if user_input:
#             ner_pipeline = pipeline("ner", grouped_entities=True)
#             entities = ner_pipeline(user_input)

#             st.write("**Named Entities:**")
#             for entity in entities:
#                 st.write(f"- **Entity:** {entity['word']} | **Type:** {entity['entity_group']} | **Score:** {entity['score']:.4f}")
#         else:
#             st.warning("Please enter some text before extracting named entities.")
# bert-base-uncased
# distilbert-base-uncased
def load_custom_model():
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"  # Replace with your fine-tuned model path or Hugging Face repo ID
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def main():
    st.title("NLP Sentiment Analysis & NER App")
    st.write("Enter text below to analyze its sentiment and extract named entities using pre-trained or fine-tuned Hugging Face models.")

    # Model selection
    model_option = st.radio("Choose a model:", ["Pretrained", "Fine-tuned"])

    # User input
    user_input = st.text_area("Enter text:")

    if st.button("Analyze Sentiment"):
        if user_input:
            if model_option == "Fine-tuned":
                sentiment_pipeline = load_custom_model()
            else:
                sentiment_pipeline = pipeline("sentiment-analysis")

            result = sentiment_pipeline(user_input)

            label = result[0]['label']
            score = result[0]['score']

            st.write(f"**Sentiment:** {label}")
            st.write(f"**Confidence Score:** {score:.4f}")
        else:
            st.warning("Please enter some text before analyzing.")

    if st.button("Extract Named Entities"):
        if user_input:
            # Use a free pretrained NER model from Hugging Face
            ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)
            
            # Perform Named Entity Recognition
            entities = ner_pipeline(user_input)
    
            st.write("**Named Entities:**")
            # Display results
            for entity in entities:
                st.write(f"- **Entity:** {entity['word']} | **Type:** {entity['entity_group']} | **Score:** {entity['score']:.4f}")
            # for entity in entities:
            #     print(f"Entity: {entity['word']}, Type: {entity['entity_group']}, Confidence: {entity['score']:.4f}")
        else:
            st.warning("Please enter some text before extracting named entities.")

# if __name__ == "__main__":
#     main()
    
    