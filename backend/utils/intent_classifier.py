from backend.utils.gemini_client import gemini_client
from backend.utils.config import GEMINI_MODEL


def classify_intent(user_query: str) -> str:
    """
    Classify the user's intent.

    Possible outputs (ONLY one word):
    greeting
    bike
    car
    health
    claim
    unknown
    """

    prompt = f"""
You are an AI Intent Classifier for an Insurance Assistant.

Your job is ONLY to classify the user's intent.

Return ONLY ONE of these labels:

greeting
bike
car
health
claim
unknown

==========================
RULES
==========================

1. Return ONLY one word.
2. No explanations.
3. No punctuation.
4. No JSON.
5. No markdown.

==========================
greeting
==========================

Use "greeting" only if the user is greeting the chatbot.

Examples:

Hi
Hello
Good morning
Hey
Good evening
How are you
Thanks
Thank you

==========================
bike
==========================

User wants a BIKE insurance quotation.

Examples:

I need bike insurance
Show bike quotation
Quote for my bike
Calculate bike premium
Buy bike insurance
Get bike policy

==========================
car
==========================

User wants a CAR insurance quotation.

Examples:

Need car insurance
Show car premium
Buy car insurance
Car quotation
Calculate car premium

==========================
health
==========================

User wants a HEALTH insurance quotation.

Examples:

Need health insurance
Health quotation
Buy health policy
Show health premium
Medical insurance

==========================
claim
==========================

IMPORTANT:

Return "claim" ONLY when the user wants to START or SUBMIT a claim.

Examples:

I met with an accident
My bike is damaged
My car is damaged
My vehicle met with an accident
File a claim
Raise a claim
Claim my insurance
Submit claim
Upload damage images
Upload accident photos
I want claim settlement
Repair claim
Vehicle damage
Broken bumper
Broken headlight
Cracked windshield
My car hit a tree

==========================
unknown
==========================

Return "unknown" for ALL insurance knowledge questions.

Examples:

What is No Claim Bonus?
Explain NCB.
What is Zero Depreciation?
What is IDV?
What is deductible?
What is engine protection?
What is cashless claim?
How does claim settlement work?
What documents are required?
What is covered?
What is not covered?
What are exclusions?
What is waiting period?
How many claims can I make?
Is flood damage covered?
Is theft covered?
What is third-party insurance?
Explain comprehensive insurance.
Tell me about bike insurance.
Tell me about car insurance.
Tell me about health insurance.
What is premium?
How is premium calculated?
Difference between comprehensive and third-party policy.
Difference between own damage and third-party.
Can I transfer my policy?
Can I renew online?

Also return "unknown" for unrelated questions.

Examples:

Who is the Prime Minister of India?
Tell me a joke.
What is Python?
Explain machine learning.

==========================
User Query
==========================

{user_query}

Return ONLY one word.
"""

    try:
        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        intent = response.text.strip().lower()

        valid_intents = [
            "greeting",
            "bike",
            "car",
            "health",
            "claim",
            "unknown"
        ]

        if intent not in valid_intents:
            return "unknown"

        return intent

    except Exception as e:
        print("Intent Classifier Error:", e)
        return "unknown"