from django.contrib import admin
from django.urls import path, include
from access import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('access/', include('access.urls')),  # Маршруты приложения access
]