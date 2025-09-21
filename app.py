from flask import Flask, render_template, request, jsonify
from src.data.loader import load_documents
from src.data.splitter import split_documents
from src.vectorstore.store import create_vectorstore
from src.chains.conversation import create_conversation_chain
from src.config.settings import KNOWLEDGE_BASE_PATH

app = Flask(__name__)

# Initialize RAG pipeline once
documents = load_documents(KNOWLEDGE_BASE_PATH)
chunks = split_documents(documents)
vectorstore = create_vectorstore(chunks)
conversation_chain = create_conversation_chain(vectorstore)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"answer": "Please ask a question."})
    
    response = conversation_chain.run(query)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
