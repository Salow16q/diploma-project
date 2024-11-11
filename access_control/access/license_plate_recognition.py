import cv2
import easyocr

def preprocess_image(image):
    # Преобразуем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применяем бинаризацию (черно-белое изображение)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Убираем шум с помощью медианного фильтра
    filtered = cv2.medianBlur(binary, 3)

    return filtered

def recognize_license_plate(image):
    # Предобработка изображения
    processed_image = preprocess_image(image)

    # Инициализация EasyOCR
    reader = easyocr.Reader(['en'])

    # Распознавание текста
    result = reader.readtext(processed_image)

    # Извлечение распознанного текста
    recognized_text = ' '.join([detection[1] for detection in result])

    return recognized_text