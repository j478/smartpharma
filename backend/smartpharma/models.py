from django.db import models

# Create your models here.
class Smartpharma(models.Model):
	prodName = models.TextField()
	prodNum = models.FloatField()
	prodColor = models.TextField()
	def __str__(self):
		return "productName: " + str(self.prodName)