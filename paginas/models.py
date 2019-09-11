from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=80)
    preco = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return self.codigo[:20]

# class Orcamento(models.Model):
#     cod_orcamento = IntegerField

# class ItemOrcamento()