from django.shortcuts import render
from .serializers import MedsSerializer, AccountSerializer
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Meds, Accounts
from passlib.hash import pbkdf2_sha256 as sha

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
    serializer_class = AccountSerializer
    queryset = Accounts.objects.all()

    def post(self, request, *args, **kwargs):
        usr = request.POST['username']
        if Accounts.userExists(Accounts, username=usr) == False:
            newPass = sha.encrypt(request.POST['password'], rounds=12000, salt_size=32)
            Accounts.objects.create(username=usr,password=newPass)

        raise PermissionDenied('Username already exists')