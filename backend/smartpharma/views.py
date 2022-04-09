from .serializers import CreateAccountSerializer, MedsSerializer
from rest_framework import viewsets
from .models import Meds, Accounts
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .authentication import Authenticator

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

@csrf_exempt
@api_view(['POST'])
def VerifyLoginView(request):
    usr = request.data.get("username")
    pswd = request.data.get("password")
    if usr is None and pswd is None:
        return Response({'error':'Please provide user & password'},
                        status=status.HTTP_400_BAD_REQUEST)
    

    account = Authenticator.authenticate(Authenticator, username=usr, password=pswd)

    if account == None:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    
    authToken = Authenticator.get_or_create(Authenticator, account)
    return Response({'token':authToken.key()},
                    status=status.HTTP_200_OK)