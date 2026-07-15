from pathlib import Path
from typing import List
from fastapi import UploadFile

"""
Validate uploaded vehicle damage images.

Returns:
{
    "valid": bool,
    "message": str
}
"""

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

MAX_FILE_SIZE = 10 * 1024 * 1024      # 10 MB

MAX_IMAGES = 6


async def validate_uploaded_images(images: List[UploadFile]) -> dict:

    # Check number of images

    if len(images) == 0:

        return {

            "valid": False,

            "message": "Please upload at least one image."

        }

    if len(images) > MAX_IMAGES:

        return {

            "valid": False,

            "message": f"You can upload a maximum of {MAX_IMAGES} images."

        }

    # Validate every image

    for image in images:

        filename = image.filename

        extension = Path(filename).suffix.lower()

        # Extension

        if extension not in ALLOWED_EXTENSIONS:

            return {

                "valid": False,

                "message": f"{filename} is not a supported image format."

            }

        # Size

        contents = await image.read()

        if len(contents) > MAX_FILE_SIZE:

            return {

                "valid": False,

                "message": f"{filename} exceeds the 10 MB size limit."

            }

        # Reset pointer

        await image.seek(0)

    return {

        "valid": True,

        "message": "All images validated successfully."

    }