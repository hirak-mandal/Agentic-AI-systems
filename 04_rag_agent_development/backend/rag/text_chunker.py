from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    all_chunks=[]
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    for doc in documents:
        chunks=splitter.split_text(doc)
        all_chunks.extend(chunks)
    return all_chunks
