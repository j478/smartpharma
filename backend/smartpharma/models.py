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
	username = models.TextField()
	password = models.TextField()

	def __str__(self):
		return "username: " + str(self.username)

	def verifyPass(self, rawPass):
		return sha.verify(rawPass, self.password)