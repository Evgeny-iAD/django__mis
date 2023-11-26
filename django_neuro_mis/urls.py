from django.contrib import admin
from django.urls import path, include
from misApp.views import get_patient_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('misApp.urls')),
    path('neuro/', include('neuroApp.urls')),
    path('path-to-your-django-view/<int:patient_id>/', get_patient_info, name='get_patient_info'),

]
