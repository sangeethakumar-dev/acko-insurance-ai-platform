from backend.utils.gemini_client import gemini_client


def classify_intent(user_query: str) -> str:
    """
    Classify whether the user is asking about
    Bike, Car or Health insurance.
    """

    prompt = f"""
You are an insurance intent classifier.

Classify the user's query into ONLY one of these labels:

bike
car
health
unknown

Rules:
- Return ONLY one word.
- Do NOT explain anything.
- Do NOT use punctuation.

User Query:
{user_query}
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    intent = response.text.strip().lower()

    return intent