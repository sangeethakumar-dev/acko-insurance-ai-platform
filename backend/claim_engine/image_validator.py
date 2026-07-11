from pathlib import Path
from fastapi import UploadFile

"""
Validate uploaded vehicle damage image.

Returns:
{
    "valid": bool,
    "message": str
}
"""

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE = 10 * 1024 * 1024


async def validate_uploaded_images(image: UploadFile) -> dict:

    filename = image.filename

    extension = Path(filename).suffix.lower()

    # Check extension
    if extension not in ALLOWED_EXTENSIONS:

        return {
            "valid": False,
            "message": f"{filename} is not a supported image format."
        }

    # Check file size
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
        "message": "Image validated successfully."
    }