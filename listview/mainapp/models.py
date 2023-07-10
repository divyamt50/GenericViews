from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    def __str__(self):
        return self.name

class Horse(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    def __str__(self):
        return self.name