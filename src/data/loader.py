import glob
import os
from langchain.document_loaders import DirectoryLoader, TextLoader
from src.exception import CustomException
import logging
import sys

def load_documents(knowledge_base_path):
    try:
        content = []
        knowledge_folders = glob.glob(f"{knowledge_base_path}/*")
        
        for folder in knowledge_folders:
            folder_name = os.path.basename(folder)
            loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, show_progress=True)
            documents = loader.load()
            for document in documents:
                document.metadata["doc_type"] = folder_name
                content.append(document)
        return content
    
    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.error({custom_error})
