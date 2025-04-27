import cv2
from app.services.thresholds import bradley_threshold, sauvola_threshold, otsu_threshold

def apply_algorithm(image, name: str):
    name = name.lower()

    if name == "otsu":
        return otsu_threshold(image)
    elif name == "bradley":
        return bradley_threshold(image)
    elif name == "sauvola":
        return sauvola_threshold(image)

    raise ValueError(f"Алгоритм '{name}' не поддерживается")


def list_algorithms():
    return ["otsu", "bradley", "sauvola"]
