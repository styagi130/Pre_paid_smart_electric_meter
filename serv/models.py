from django.db import models
# Create your models here.


class police(models.Model):
	user=models.CharField(max_length=100, default='192.168.43.263',null=True,blank=True)
	passwd=models.CharField(max_length=100, default='raspberry',null=True,blank=True)
	add=models.CharField(max_length=20, default='192.168.43.236')
	money=models.IntegerField(default=0)

	def __str__(self):
		return self.add

	def add_money(self,mone, *args, **kwargs):
		self.money+=mone
		return self.money