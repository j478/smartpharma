from django.db import models
from passlib.hash import pbkdf2_sha256 as sha

# Create your models here.
class Meds(models.Model):
	prodName = models.TextField()
	amtPerscribed = models.IntegerField()
	amtInStock = models.IntegerField()

	def __str__(self):
		return "productName: " + str(self.prodName)

class Accounts(models.Model):
	username = models.TextField(unique=True)
	password = models.TextField()

	def usernameString(self):
		return str(self.username)

	def __str__(self):
		return "username: " + str(self.username)

	def verifyPass(self, rawPass):
		return sha.verify(rawPass, self.password)

class authTokens(models.Model):
	token = models.CharField(unique=True, max_length=40)
	user = models.TextField()
	dateTime = models.CharField(max_length=40)

	def __str__(self):
		return "token: " + str(self.token)

	def key(self):
		return str(self.token)