from django.urls import path
from . import views

urlpatterns = [
    path('check_access/', views.check_access, name='check_access'),
]