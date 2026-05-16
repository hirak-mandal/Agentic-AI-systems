import faiss 
import numpy as np
from sentence_transformers import SentenceTransformer

#embedding model
model=SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query,chunks,top_k=2):
    #loading faiss database
    index=faiss.read_index("data/faiss_index/index.bin")
    #query embeddings
    query_embedding=model.encode([query])
    #converting embeddinss into float32 numpy array
    query_embedding=np.array(query_embedding).astype("float32")
    #searching similaritu vectors(SEMANTIC SEARCH)
    distances, indices = index.search(query_embedding, top_k)
    #collecting matched chunks
    retreived_chunks=[]
    #suppose --> indeces=[[4,1]] --> chunk[4] and chunk[1] is similar
    for i in indices[0]:
        retreived_chunks.append(chunks[i])
    return retreived_chunks