import os
from typing import Any
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as PineconeLangchain

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def run_llm(query: str) -> Any:
    embeddings = OpenAIEmbeddings()
    docsearch = PineconeLangchain.from_existing_index(
        embedding=embeddings, index_name="langchain-doc-index"
    )
    chat = ChatOpenAI(verbose=True, temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )
    return qa.invoke({"query": query})

if __name__ == "__main__":
    query = "What is the Langchain?"
    print(run_llm(query))