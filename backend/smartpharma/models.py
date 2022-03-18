from django.db import models

# Create your models here.
class Meds(models.Model):
	prodNum = models.IntegerField()
	prodName = models.TextField()
	amtInStock = models.IntegerField()

	def __str__(self):
		return "productName: " + str(self.prodName)