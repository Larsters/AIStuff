import os
from typing import Any, List
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as PineconeLangchain


pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def run_llm(query: str, chat_history: List[tuple[str, Any]] = []) -> Any:
    embeddings = OpenAIEmbeddings()
    docsearch = PineconeLangchain.from_existing_index(
        embedding=embeddings, index_name="langchain-doc-index"
    )
    chat = ChatOpenAI(verbose=True, temperature=0)

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=docsearch.as_retriever(), return_source_documents=True
    )

    return qa({"question": query, "chat_history": chat_history})


if __name__ == "__main__":
    query = "What is the Langchain?"
    print(run_llm(query))
