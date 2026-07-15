from backend.utils.gemini_client import gemini_client


def classify_intent(user_query: str) -> str:
    """
    Classify whether the user is asking about
    Bike, Car, Health insurance or Claim.
    """

    prompt = f"""
You are an insurance intent classifier.

Classify the user's query into ONLY one of these labels:

bike
car
health
claim
unknown

Rules:
- Return ONLY one word.
- Do NOT explain anything.
- Do NOT use punctuation.

Examples:

"I need bike insurance"
bike

"Show bike quotation"
bike

"I want car insurance"
car

"Need health policy"
health

"My car met with an accident"
claim

"I want to file a claim"
claim

"My bike is damaged"
claim

"Upload damage photos"
claim

"I need claim settlement"
claim

User Query:
{user_query}
"""

    try:
        response = gemini_client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    except Exception as e:
        print("Intent Classifier Error:", e)
        return "general"


    intent = response.text.strip().lower()

    return intent