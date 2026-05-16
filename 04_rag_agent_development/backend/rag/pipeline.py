from utils.file_loader import document_loader
from rag.text_chunker import chunk_documents
from rag.embedder import embed_chunks
from rag.faiss_store import store_embeddings

documents=document_loader()
chunks=chunk_documents(documents)
embeddings=embed_chunks(chunks)
faiss_index=store_embeddings(embeddings)