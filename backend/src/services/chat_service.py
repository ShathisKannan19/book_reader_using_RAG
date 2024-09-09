from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import os

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Hey! If you don't have context do not mention like this `I don't see any context from books mentioned`,
Use the following context from the books to answer the question:

Context:
{context}

Sources:
{sources}

---

User's question: {question}

---
#Important
    - If it was a big paragraph you must make it breakdown and also gave as in Markdown format.
    - Provide an answer based on the above context. If multiple books are referenced, mention their names. Speak like a friend.
    - If any context is not mentioned speak like a friend and motivator you give or suggest to speak like this and mention you are the guy like self developing quote. 
    - If Don't have context you do not mention as we don't have context in chat, coverse normally.
    - You must give any of the mentionable thing you must give that in mentioning tag like `hugging face` If i ask about Hugging Face.
    - If you want mention anything use this `` instead of ""
"""

CHROMA_PATH = os.path.realpath(filename="./src/chroma")

def get_embedding_function():
    embedding_model = "mixedbread-ai/mxbai-embed-large-v1"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    return embeddings

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    sources = [doc.metadata.get("id", None) for doc, _score in results]

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text, sources= sources)
    # print(prompt)

    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        # other params...
        )
    response_text = llm.invoke(prompt)

    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text

def chat_service_response(query_text):
    res = query_rag(query_text)
    response = res.content
    return response