def build_prompt(user_query, top_3_chunks):
    context = ""

    for score, chunk, metadata in top_3_chunks:
        context += f"""
        Source: {metadata['pdf_name']}
        Section: {metadata.get('section_title', metadata.get('section', 'N/A'))}

        {chunk}

        """
    
    prompt = f"""
        You are Acko Insurance AI Assistant.

        Answer the user's insurance-related questions using ONLY the provided context.

        Rules:
        1.Do not use external knowledge.
        2.Do not make assumptions.
        3.Only answer from provided context.
        4. If answer is not available, say:
        "Sorry, I couldn't find this information in the policy documents."
        5. Be clear and concise.
        6. Mention policy details when relevant.
        7. Give response in simple user-friendly language.
        8. If possible, mention which policy document the answer came from.
        Context:
            {context}
        User Question:
            {user_query}
            """
    return prompt