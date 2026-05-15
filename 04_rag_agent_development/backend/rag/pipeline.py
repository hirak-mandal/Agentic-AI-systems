from utils.file_loader import document_loader
from rag.text_chunker import chunk_documents
from rag.embedder import embed_chunks

documents=document_loader()
chunks=chunk_documents(documents)
embeddings=embed_chunks(chunks)