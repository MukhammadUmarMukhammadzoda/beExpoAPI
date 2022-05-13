from distutils.command.upload import upload
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Ari(models.Model):
    nomi = models.CharField(max_length=50, blank=True, null=True)
    rasmi = models.ImageField(upload_to = 'images')
    video_link = models.CharField(max_length=150, blank=True)
    narxi = models.FloatField()
    malumot = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.nomi

    objects: models.Manager()



class Asal(models.Model):
    nomi = models.CharField(max_length=50, blank=True, null=True)
    rasmi = models.ImageField(upload_to = 'images')
    video_link = models.CharField(max_length=150, blank=True)
    narxi = models.FloatField()
    malumot = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nomi
    
    objects: models.Manager()


class Company(models.Model):
    nomi = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nomeri = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.nomi


class Klient(models.Model):
    ismi = models.CharField(max_length=100, blank=True, null=True)
    rasmi = models.ImageField(upload_to = 'images')
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ismi



