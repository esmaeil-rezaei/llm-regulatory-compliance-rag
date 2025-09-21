from langchain.text_splitter import CharacterTextSplitter
from src.exception import CustomException
from src.config.settings import CHUNK_SIZE, CHUNK_OVERLAP
import logging
import sys

def split_documents(documents):
    try:
        text_splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        logging.info(f"chunk len is {len(text_splitter.split_documents(documents))}")
        return text_splitter.split_documents(documents)
    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.error({custom_error})
