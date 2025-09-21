import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OpenAI_API_KEY")
DB_NAME = "vector_db"
MODEL_NAME = "gpt-3.5-turbo"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
KNOWLEDGE_BASE_PATH = "knowledgebase"