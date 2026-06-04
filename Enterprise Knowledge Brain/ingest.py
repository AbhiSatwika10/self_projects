from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

loader = PyPDFLoader("data/company_policy.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

vectordb = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="chroma_db"
)

vectordb.persist()

print("Documents Indexed Successfully")
