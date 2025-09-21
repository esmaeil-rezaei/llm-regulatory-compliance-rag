from src.data.loader import load_documents
from src.data.splitter import split_documents
from src.vectorstore.store import create_vectorstore
from src.chains.conversation import create_conversation_chain
from src.interface.gradio_ui import launch_chat
from src.config.settings import KNOWLEDGE_BASE_PATH

def main():
    documents = load_documents(KNOWLEDGE_BASE_PATH)
    chunks = split_documents(documents)
    vectorstore = create_vectorstore(chunks)
    conversation_chain = create_conversation_chain(vectorstore)
    launch_chat(conversation_chain)

if __name__ == "__main__":
    main()
