from django.urls import path
from .api import CreateSchools

app_name = 'schools'

urlpatterns = [
    path('', CreateSchools.as_view(), name='list')
]