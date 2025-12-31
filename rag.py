from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

DB_PATH = "db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

llm = OllamaLLM(
    model="llama3.2:1b",
    temperature=0,
    num_ctx=2048
)

chat_history = []

response_cache = {}

def chatbot_ask(query: str) -> str:
    global chat_history, response_cache

    if query in response_cache:
        return response_cache[query]

    results = vectordb.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in results])[:3000]

    history_str = "\n".join(chat_history[-4:])

    prompt = f"""
You are a helpful assistant. Use the document context to answer accurately.

### CHAT HISTORY:
{history_str}

### DOCUMENT CONTEXT:
{context}

### QUESTION:
{query}

### ANSWER:
"""

    response = llm.invoke(prompt)

    response_cache[query] = response

    chat_history.append(f"Human: {query}")
    chat_history.append(f"AI: {response}")

    return response


if __name__ == "__main__":
    print("🤖 PDF RAG Chatbot (type 'exit' to quit)")
    while True:
        q = input("\nYou: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("\nAI:", chatbot_ask(q))
