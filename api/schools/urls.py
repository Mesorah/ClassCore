from django.urls import path
from .api import CreateUsers

urlpatterns = [
    path('', CreateUsers.as_view(), name='user-list')
]