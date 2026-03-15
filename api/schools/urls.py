from django.urls import path
from .api import CreateSchools

urlpatterns = [
    path('', CreateSchools.as_view(), name='user-list')
]