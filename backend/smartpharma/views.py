from .serializers import AuthTokenSerializer, CreateAccountSerializer, MedsSerializer, VerifyLoginSerializer, AuthTokenSerializer
from rest_framework import viewsets
from .models import Meds, Accounts, AuthTokens
from rest_framework.response import Response
from rest_framework import status
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

class VerifyLoginView(viewsets.GenericViewSet):
    serializer_class = VerifyLoginSerializer
    queryset = Accounts.objects.all()

    def create(self, request, *args, **kwargs):
        usr = request.data.get("username")
        pswd = request.data.get("password")

        if usr is None and pswd is None:
            return Response({'error':'Please provide user & password'},status=status.HTTP_400_BAD_REQUEST)
        account = Authenticator.authenticate(Authenticator, username=usr, password=pswd)

        if account == None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    
        authToken = Authenticator.get_or_create(Authenticator, account)
        response = Response({'success':'login successful', 'token':authToken.key()}, status=status.HTTP_200_OK)
        return response

class VerifyTokenView(viewsets.GenericViewSet):
    serializer_class = AuthTokenSerializer
    queryset = AuthTokens.objects.all()

    def create(self, request, *args, **kwargs):
        account = Authenticator.get_account_with_token(Authenticator, request.data.get('token'))
        
        if account != None:
            username = account.usernameString()
            email = account.emailString()
            phoneNumber = account.phoneNumString()
            print(phoneNumber)

            return Response({'username':username, 'email':email, 'phone_number':phoneNumber}, status=status.HTTP_200_OK)

        return Response({'error':'no matching token for user'}, status=status.HTTP_418_IM_A_TEAPOT)

class LogoutView(viewsets.GenericViewSet):
    serializer_class = AuthTokenSerializer
    queryset = AuthTokens.objects.all()

    def create(self, request, *args, **kwargs):
        success = Authenticator.logout_token(Authenticator, request.data.get('token'))
        if success:
            return Response({'logout-status':'successful'}, status=status.HTTP_200_OK)
        
        return Response({'logout-status':'something went wrong. user may not be successfully logged-out'}, status=status.HTTP_418_IM_A_TEAPOT)
            