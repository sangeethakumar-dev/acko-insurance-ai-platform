from google import genai
from backend.utils.config import GEMINI_API_KEY
import chromadb

#Gemini Client

gemini_client = genai.Client(
    api_key = GEMINI_API_KEY
)

#Choroma Client 

chroma_client = chromadb.PersistentClient(path="./chroma_db")

#Chroma Collection 

collection = chroma_client.get_or_create_collection(
        name="pdf_collection"
        )


#Question Embedding

def get_query_embedding(user_query):
    result = gemini_client.models.embed_content(
                model="gemini-embedding-2",
                contents=user_query             
                )
    query_embedding = result.embeddings[0].values
    return query_embedding

#Retrieving Chunks from ChromaDB

def retrieve_context(query_embedding):
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5,
        include=["documents", "metadatas", "distances"]
    )
    retrieved_distances = results['distances'][0]
    retrieved_chunks = results["documents"][0] 
    retrieved_metadata = results["metadatas"][0]

    print("Retrieved Top 5 Chunks")
    return retrieved_chunks,retrieved_metadata,retrieved_distances

#Re-rank Chunks

def rerank_chunks(user_query, retrieved_chunks,retrieved_metadata):
    
    scored_chunks = []

    query_words = set(user_query.lower().split())

    for chunk,metadata in zip(retrieved_chunks,retrieved_metadata):
        
        chunk_words = set(chunk.lower().split())

        #keyword-overlap based reranking

        score = len(query_words.intersection(chunk_words))

        scored_chunks.append((score, chunk,metadata))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    top_3_chunks = scored_chunks[:3]

    print("Reranked Top 3 Chunks")

    return top_3_chunks

#Retrieving Pipeline

def retrieve_pipeline(user_query):
    query_embedding = get_query_embedding(user_query)

    retrieved_chunks, retrieved_metadata, retrieved_distances = retrieve_context(query_embedding)

    top_3_chunks = rerank_chunks(
        user_query,
        retrieved_chunks,
        retrieved_metadata
    )

    return top_3_chunks