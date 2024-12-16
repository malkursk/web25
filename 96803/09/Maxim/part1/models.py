from django.db import models

class Owner(models.Model):
    fio = models.CharField(max_length=150)
    born = models.DateField()

class Car(models.Model):
    brand = models.CharField(max_length=50)
    number = models.CharField(max_length=6)
    region = models.IntegerField(max_length=3)
    registration = models.DateField()

class Result(models.Model):
    sam = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
