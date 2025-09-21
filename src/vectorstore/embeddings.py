from langchain_openai import OpenAIEmbeddings
from src.config.settings import API_KEY

def get_embeddings():
    return OpenAIEmbeddings(api_key=API_KEY)
