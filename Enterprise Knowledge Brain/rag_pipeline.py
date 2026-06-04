from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def ask_question(query):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(model="gpt-4o-mini")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa.run(query)
