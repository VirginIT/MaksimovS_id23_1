import cv2
import numpy as np
import base64
from app.services.algorithms import apply_algorithm

def decode_base64_image(base64_string: str) -> np.ndarray:
    image_data = base64.b64decode(base64_string)
    np_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Невозможно декодировать изображение")
    return image

def encode_image_to_base64(image: np.ndarray) -> str:
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

def binarize_image(image_base64: str, algorithm: str) -> str:
    image = decode_base64_image(image_base64)
    binary_image = apply_algorithm(image, algorithm)
    return encode_image_to_base64(binary_image)


