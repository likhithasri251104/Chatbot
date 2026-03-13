import numpy as np
from models.embeddings import get_embedding

documents = []
vectors = []

def load_documents():
    global documents, vectors

    with open("documents/knowledge.txt", "r") as f:
        docs = f.readlines()

    documents = docs
    vectors = [get_embedding(doc) for doc in docs]


def retrieve_context(query):
    query_vec = get_embedding(query)

    scores = [np.dot(query_vec, v) for v in vectors]

    best_index = np.argmax(scores)

    return documents[best_index]
