import faiss
import numpy as np

def store_embeddings(embeddings):
    #converting embeddings into numpy array
    #faiss wants 32-bit float for vectorization
    embeddings=np.array(embeddings).astype("float32")

    #dimension of embedding
    #suppose (20,384):
    #20 --> no. of vectors--> no. of chunked text
    #384 -->(x1,x2,x3,x4......)--> dimension for storing vector
    dimension=embeddings.shape[1]

    #creating faiss index
    index=faiss.IndexFlatL2(dimension)

    #adding vectors in faiss index
    index.add(embeddings)

    #saving vectors locally
    #otherwise if computer loaded past memory will erase
    faiss.write_index(index,"data/faiss_index/index.bin")

    return index