from django.shortcuts import render
from .forms import ImageUploadForm
from .license_plate_recognition import recognize_license_plate
from .models import Event
import cv2
import numpy as np
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def home(request):
    return render(request, 'access/home.html')

def check_access(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохранение загруженного изображения
            image_file = request.FILES['image']
            image_path = default_storage.save('temp.jpg', ContentFile(image_file.read()))
            image_url = default_storage.url(image_path)

            # Чтение изображения с помощью OpenCV
            image = cv2.imread(image_url[1:])  # Убираем первый символ '/'

            # Распознавание гос. номера
            license_plate = recognize_license_plate(image)

            # Создание события
            event = Event.objects.create(
                license_plate=license_plate,
                allowed=True,  # Здесь можно добавить логику проверки доступа
                image=image_file
            )

            return render(request, 'access/check_access.html', {'license_plate': license_plate, 'image_url': image_url})
    else:
        form = ImageUploadForm()

    # Получение последних 10 событий
    events = Event.objects.order_by('-timestamp')[:10]
    return render(request, 'access/check_access.html', {'form': form, 'events': events})