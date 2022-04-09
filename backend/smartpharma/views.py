from django.shortcuts import render
from .serializers import CreateAccountSerializer, MedsSerializer, AccountSerializer
from rest_framework import viewsets
from .models import Meds, Accounts

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

    def get(self, request, *args, **kwargs):
        #serializer = MedsSerializer(instance=self.queryset)
        #data = serializer.data
        #return Response(data)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CreateAccountView(viewsets.ModelViewSet):
    serializer_class = CreateAccountSerializer
    queryset = Accounts.objects.all()

class VerifyLoginView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Accounts.objects.all()