from django.urls import path
from .views import mis, MisWork

urlpatterns = [
    path('', MisWork.as_view(), name='MisWork'),
    path('mis/', mis, name='mis'),
]
