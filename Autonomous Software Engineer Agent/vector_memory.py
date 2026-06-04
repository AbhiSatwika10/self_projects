from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = OpenAIEmbeddings()

vectordb = Chroma(
    persist_directory="memory_db",
    embedding_function=embeddings
)
