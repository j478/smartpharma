from hashlib import new
from .models import Accounts
from .models import AuthTokens
from secrets import token_urlsafe
from datetime import datetime

class Authenticator:
    def authenticate(self, username, password):
        try:
            target = Accounts.objects.get(username=username)
            if Accounts.verifyPass(target,password):
                return target
            else:
                return None
        except Accounts.DoesNotExist:
            return None
    
    def get_or_create(self, account):
        try:
            currentAuthToken = AuthTokens.objects.get(user=Accounts.usernameString(account))
            return currentAuthToken
        except AuthTokens.DoesNotExist:
            newAuthToken = AuthTokens.objects.create(
                token = token_urlsafe(20),
                user = Accounts.usernameString(account),
                dateTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            )

            return newAuthToken
    
    def get_account_with_token(self, inToken):
        try:
            tokenUser = AuthTokens.objects.get(token=inToken)
            user = tokenUser.userString()
            return Accounts.objects.get(username=user)
        except AuthTokens.DoesNotExist:
            return None

    def logout_token(self, inToken):
        try:
            tokenUser = AuthTokens.objects.get(token=inToken)
            tokenUser.delete()
            return True
        except AuthTokens.DoesNotExist:
            return False
        