from django.db import models

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

	def userExists(self, username):
		try:
			self.objects.get(username=username)
			return True 
		except self.DoesNotExist:
			return False