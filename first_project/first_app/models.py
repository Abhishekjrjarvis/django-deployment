from django.db import models

# Create your models here.
class Topic(models.Model):
	top_name = models.CharField(max_length=264,unique=True)

	def __str__(self):
		return self.top_name


class Webpage(models.Model):
	topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
	name = models.CharField(max_length=264)
	url = models.URLField()

	def __str__(self):
		return self.name


class AccessRecord(models.Model):
	title = models.ForeignKey(Webpage, on_delete= models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return self.date