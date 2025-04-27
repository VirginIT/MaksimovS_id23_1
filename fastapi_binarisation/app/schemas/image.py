from pydantic import BaseModel

class ImageRequest(BaseModel):
    image: str  # base64 string
    algorithm: str  # например, "otsu"

class ImageResponse(BaseModel):
    binarized_image: str  # base64 string
