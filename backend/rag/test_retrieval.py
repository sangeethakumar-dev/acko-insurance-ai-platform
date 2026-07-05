from backend.rag.retrieval import *

query = "What is zero depreciation insurance?"

query_embedding = get_query_embedding(query)

retrieved_chunks, retrieved_metadata, retrieved_distances = retrieve_context(query_embedding)

top_3 = rerank_chunks(query, retrieved_chunks, retrieved_metadata)

for idx, (score, chunk, metadata) in enumerate(top_3):
    print(f"\nChunk {idx+1}")
    print(f"Score: {score}")
    print(f"Metadata: {metadata}")
    print(f"Text: {chunk[:500]}")