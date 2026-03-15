from rest_framework.generics import ListCreateAPIView
from .models import School
from .serializers import SchoolSerializer



class CreateSchools(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer