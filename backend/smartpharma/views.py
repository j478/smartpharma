from django.shortcuts import render
from .serializers import MedsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Meds

# Create your views here.
class MedsView(viewsets.ModelViewSet):
    serializer_class = MedsSerializer
    queryset = Meds.objects.all()

    """
    def get_queryset(self):
        length = self.request.query_params.get('len')
        if length is not None:
            return Meds.objects.order_by('prodNum')[0:int(length)]
    """

    def get(self, request, *args, **kwagrgs):
        serializer = MedsSerializer(instance=self.queryset)
        data = serializer.data
        return Response(data)

    def post():
        asdf = 1