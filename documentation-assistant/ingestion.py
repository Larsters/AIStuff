import os
from dotenv import load_dotenv
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeLangchain
from pinecone import Pinecone


load_dotenv()


def ingest_data() -> None:
    print("Ingesting data...")
    loader = ReadTheDocsLoader(
        path="langchain-docs/api.python.langchain.com/en/latest/_modules/langchain"
    )
    raw_data = loader.load()
    print(f"loaded {len(raw_data)} documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        separators=["\n\n", "\n", " ", ".", ","],
    )
    documents = text_splitter.split_documents(documents=raw_data)
    print(f"split into {len(documents)} chunks")

    for doc in documents:
        old_path = doc.metadata["source"]
        new_path = old_path.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_path})

    print(f"Inserting {len(documents)} documents into pinecone")
    embeddings = OpenAIEmbeddings()
    PineconeLangchain.from_documents(
        documents=documents, embedding=embeddings, index_name="langchain-doc-index"
    )
    print("Data ingested and added to Pinecone vectorstore vectors")


if __name__ == "__main__":
    ingest_data()
