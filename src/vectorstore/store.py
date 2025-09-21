from langchain.vectorstores import FAISS
from src.exception import CustomException
from .embeddings import get_embeddings
import logging
import sys

def create_vectorstore(chunks):
    try:
        embeddings = get_embeddings()
        vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
        logging.info(f"Total vectors: {vectorstore.index.ntotal}")
        logging.info(f"Vector dimension: {vectorstore.index.d}")
        return vectorstore
    
    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.error({custom_error})