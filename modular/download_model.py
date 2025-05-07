from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer, AutoModelForTokenClassification

# Clear the cache manually or force a re-download
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER", force_download=True)
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER", force_download=True)