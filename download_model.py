from transformers import pipeline

# Download the model files and save them to ./local-flan-t5-small
pipe = pipeline("text2text-generation", model="google/flan-t5-small")
pipe.save_pretrained("./local-flan-t5-small")