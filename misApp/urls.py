from django.urls import path
from .views import MisWork

urlpatterns = [
    path('', MisWork.as_view(), name='MisWork'),
]
