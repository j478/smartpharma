from hashlib import new
from .models import Accounts
from .models import authTokens
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
            currentAuthToken = authTokens.objects.get(user=Accounts.usernameString(account))
            return currentAuthToken
        except authTokens.DoesNotExist:
            newAuthToken = authTokens.objects.create(
                token = token_urlsafe(20),
                user = Accounts.usernameString(account),
                dateTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            )

            return newAuthToken