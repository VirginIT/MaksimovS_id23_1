import numpy as np
import cv2

def bradley_threshold(image: np.ndarray, t: float = 0.15) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    S = gray.shape[1] // 8
    s2 = S // 2
    integral_image = cv2.integral(gray, sdepth=cv2.CV_64F)
    binary_image = np.zeros_like(gray, dtype=np.uint8)

    height, width = gray.shape
    for i in range(width):
        for j in range(height):
            x1 = max(i - s2, 0)
            x2 = min(i + s2, width - 1)
            y1 = max(j - s2, 0)
            y2 = min(j + s2, height - 1)
            count = (x2 - x1) * (y2 - y1)
            sum_region = (integral_image[y2 + 1, x2 + 1] - integral_image[y1, x2 + 1] -
                          integral_image[y2 + 1, x1] + integral_image[y1, x1])
            if int(gray[j, i]) * count < sum_region * (1.0 - t):
                binary_image[j, i] = 0
            else:
                binary_image[j, i] = 255
    return binary_image
#
# def bradley_threshold(image: np.ndarray, t: float = 0.15) -> np.ndarray:
#     """Адаптивная бинаризация по методу Брэдли (без использования cv2.integral)."""
#     # Перевод в градации серого
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     height, width = gray.shape
#
#     # Размер окна (пропорционален ширине)
#     S = width // 8
#     s2 = S // 2
#
#     # Создание интегрального изображения вручную
#     integral = np.zeros_like(gray, dtype=np.float64)
#     for y in range(height):
#         for x in range(width):
#             integral[y, x] = gray[y, x]
#             if y > 0:
#                 integral[y, x] += integral[y - 1, x]
#             if x > 0:
#                 integral[y, x] += integral[y, x - 1]
#             if x > 0 and y > 0:
#                 integral[y, x] -= integral[y - 1, x - 1]
#
#     # Результирующее бинарное изображение
#     binary_image = np.zeros_like(gray, dtype=np.uint8)
#
#     for y in range(height):
#         y1 = max(y - s2, 0)
#         y2 = min(y + s2, height - 1)
#
#         for x in range(width):
#             x1 = max(x - s2, 0)
#             x2 = min(x + s2, width - 1)
#
#             count = (x2 - x1 + 1) * (y2 - y1 + 1)
#
#             # Сумма яркости в окне
#             A = integral[y2, x2]
#             B = integral[y1 - 1, x2] if y1 > 0 else 0
#             C = integral[y2, x1 - 1] if x1 > 0 else 0
#             D = integral[y1 - 1, x1 - 1] if y1 > 0 and x1 > 0 else 0
#             sum_region = A - B - C + D
#
#             if gray[y, x] * count < sum_region * (1.0 - t):
#                 binary_image[y, x] = 0
#             else:
#                 binary_image[y, x] = 255
#
#     return binary_image


def sauvola_threshold(image: np.ndarray, window_size: int = 25, k: float = 0.8) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean = cv2.boxFilter(gray, ddepth=cv2.CV_64F, ksize=(window_size, window_size))
    sqmean = cv2.boxFilter(np.square(gray), ddepth=cv2.CV_64F, ksize=(window_size, window_size))
    stddev = np.sqrt(sqmean - np.square(mean))

    threshold = mean * (1 + k * ((stddev / 128) - 1))
    binary = np.where(gray > threshold, 255, 0).astype(np.uint8)
    return binary

def otsu_threshold(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

