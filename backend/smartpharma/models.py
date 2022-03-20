from django.db import models

# Create your models here.
class Meds(models.Model):
	prodName = models.TextField()
	amtPerscribed = models.IntegerField()
	amtInStock = models.IntegerField()

	def __str__(self):
		return "productName: " + str(self.prodName)