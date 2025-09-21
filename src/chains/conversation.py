from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from src.config.settings import API_KEY, MODEL_NAME
from src.exception import CustomException
import logging
import sys

def create_conversation_chain(vectorstore):
    try:
        llm = ChatOpenAI(api_key=API_KEY, temperature=0.7, model_name=MODEL_NAME)
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        retriever = vectorstore.as_retriever()
        return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.error({custom_error})