from fastapi import APIRouter, HTTPException
from app.schemas.image import ImageRequest, ImageResponse
from app.services.binarization import binarize_image
from app.services.algorithms import list_algorithms

router = APIRouter()

@router.post("/binary_image/", response_model=ImageResponse)
def process_image(request: ImageRequest):
    try:
        result = binarize_image(request.image, request.algorithm.lower())
        return {"binarized_image": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/algorithms/")
def get_supported_algorithms():
    return {"available_algorithms": list_algorithms()}
