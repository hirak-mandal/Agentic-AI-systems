from llm.gemini_client import client
from core.prompts import system_prompt
from rag.retriever import retrieve_chunks
from rag.pipeline import chunks

def llm_response(query):
    #searched chunks which are similar to user query
    similar_chunks=retrieve_chunks(query,chunks)
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt + "\nUser query" + query + "\ncontext\n" + "\n".join(similar_chunks)
    )
    return response.text