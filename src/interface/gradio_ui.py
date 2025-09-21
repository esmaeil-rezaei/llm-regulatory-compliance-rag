import gradio as gr
from src.exception import CustomException
import logging
import sys

def launch_chat(conversation_chain):
    try:
        def chat(message, history):
            result = conversation_chain.invoke({"question": message})
            return result["answer"]

        gr.ChatInterface(chat, type="messages").launch()

    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.error({custom_error})