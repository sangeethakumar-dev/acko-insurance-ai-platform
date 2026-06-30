
def rerank_chunks(query, retrieved_chunks):
    scored_chunks = []

    query_words = set(query.lower().split())

    for chunk in retrieved_chunks:
        chunk_text = chunk.lower()
        chunk_words = set(chunk_text.split())

        score = len(query_words.intersection(chunk_words))

        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    top_3 = [chunk for score, chunk in scored_chunks[:3]]

    return top_3

def retrieve_context(query, collection):
    
    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    retrieved_chunks = results["documents"][0]

    top_chunks = rerank_chunks(query, retrieved_chunks)

    return top_chunks