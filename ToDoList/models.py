from django.db import models
from django.conf import settings

class Lista(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    archivado = models.BooleanField(default=False)

    def __str__(self):
        return self.texto


# Create your models here.
