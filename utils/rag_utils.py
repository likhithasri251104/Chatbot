import numpy as np
from models.embeddings import get_embedding

documents = []
vectors = []

def load_documents():
    global documents, vectors

    with open("documents/knowledge.txt", "r") as f:
        docs = f.readlines()

    documents = [doc.strip() for doc in docs if doc.strip()]
    vectors = [get_embedding(doc) for doc in documents]


def retrieve_context(query):
    global documents, vectors

    if len(documents) == 0:
        return "No documents loaded."

    query_vec = get_embedding(query)

    scores = [np.dot(query_vec, v) for v in vectors]

    best_index = int(np.argmax(scores))

    return documents[best_index]
