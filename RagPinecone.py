from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["PINECONE_API_KEY"] = "4ce1743e-57db-4a13-9809-530ec8c90e32"
os.environ["PINECONE_ENV"] = "gcp-starter"

def loadText():
    loader = TextLoader("../iglesia_Dios.txt")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
    )
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    import pinecone
    # initialize pinecone
    pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV"),
    )
    index_name = "langchain-demo"
    # First, check if our index already exists. If it doesn't, we create it
    if index_name not in pinecone.list_indexes():
        # we create a new index
        pinecone.create_index(name=index_name, metric="cosine", dimension=1536)
        print("Index created:", index_name)
        # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
        docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
        # Llama a la función para cargar los documentos

def search():
    embeddings = OpenAIEmbeddings()
    import pinecone
    # initialize pinecone
    pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV"),
    )
    index_name = "langchain-demo"
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    query = "Cuando se creo la iglesia?"
    docs = docsearch.similarity_search(query)
    if docs:
        print(docs[0].page_content)
    else:
        print("No documents found for the query.")
loadText()
search()