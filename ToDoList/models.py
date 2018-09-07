from django.db import models
from django.conf import settings



class Lista(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField()


    def __str__(self):
        return self.texto


# Create your models here.
