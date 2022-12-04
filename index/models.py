from django.db import models
class about(models.Model):
    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=800,blank=False)
    images = models.ImageField(upload_to='about/',blank=False)
    def __str__(self):
        return self.title
class slider(models.Model):
    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=800,blank=False)
    images = models.ImageField(upload_to='slider/',blank=False)
    def __str__(self):
        return self.title
class client(models.Model):
    name = models.CharField(max_length=200,blank=False)
    link = models.CharField(max_length=200,blank=False)
    images = models.ImageField(upload_to='client/',blank=False)
    def __str__(self):
        return self.name
# Create your models here.
