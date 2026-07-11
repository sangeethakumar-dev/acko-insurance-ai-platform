import json
from pathlib import Path

from importlib_resources import contents

from backend.utils.gemini_client import gemini_client
from backend.utils.prompt_builder import build_claim_analysis_prompt

from google.genai import types

"""
Analyze uploaded vehicle damage images using Gemini Vision.

Parameters
    image_paths : list[str]
        List of uploaded image paths.

Returns
    dict
        Vehicle and damage details extracted by Gemini.
"""


def analyze_images(image_paths: list[str]) -> dict:

    # Build the prompt
    prompt = build_claim_analysis_prompt()

    # Prepare Gemini input
    contents = [prompt]

    for image_path in image_paths:

        image_path = Path(image_path)

        with open(image_path, "rb") as image_file:

            image_bytes = image_file.read()

        

        contents.append(
        types.Part.from_bytes(
        data=image_bytes,
        mime_type="image/jpeg"
    )
)

    # Gemini Vision
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
    )

    response_text = response.text.strip()

    # Remove markdown if Gemini returns it
    response_text = (
        response_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    # Convert JSON string → Python Dictionary
    try:

        analysis = json.loads(response_text)

    except Exception:

        analysis = {
            "vehicle_type": "",
            "brand": "",
            "model": "",
            "color": "",
            "segment": "",
            "incident_type": "",
            "damage_type": "",
            "severity": 0,
            "affected_parts": [],
            "estimated_repair_cost": 0,
            "fraud_risk": "UNKNOWN",
            "summary": response_text,
        }

    return analysis