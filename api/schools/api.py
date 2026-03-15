from rest_framework.generics import ListCreateAPIView
from .models import School
from .serializers import SchoolSerializer



class CreateUsers(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer