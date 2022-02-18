from django.shortcuts import render
from .serializers import SmartpharmaSerializer
from rest_framework import viewsets
from .models import Smartpharma

# Create your views here.
class SmartpharmaView(viewsets.ModelViewSet):
    serializer_class = SmartpharmaSerializer
    queryset = None

    def get_queryset(self):
        length = self.request.query_params.get('len')
        if length is not None:
            return Smartpharma.objects.order_by('prodNum')[0:int(length)]
