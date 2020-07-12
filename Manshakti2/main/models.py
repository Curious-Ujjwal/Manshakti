from django.db import models
from django.utils import timezone


# Create your models here.
class Story(models.Model):
	name = models.CharField(max_length=30, blank=True , default="")
	city = models.CharField(max_length=12)
	inbox = models.TextField(max_length=3500)
	subject = models.CharField(max_length=90, default="")
	admin_approved=models.BooleanField(default="False")
	pub_date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.inbox[:]