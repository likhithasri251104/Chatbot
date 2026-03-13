from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from models.embeddings import get_embedding_model

def build_vector_database():

    loader = TextLoader("documents/knowledge.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embedding_model()

    vector_db = FAISS.from_documents(chunks, embeddings)

    return vector_db


def retrieve_context(query, vector_db):

    results = vector_db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in results])

    return context
