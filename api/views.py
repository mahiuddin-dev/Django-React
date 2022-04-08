from rest_framework.generics import ListAPIView
# Create your views here.
from .models import Person
from .serializers import PersonSerializer

class IndexView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
