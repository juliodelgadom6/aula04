from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=60)