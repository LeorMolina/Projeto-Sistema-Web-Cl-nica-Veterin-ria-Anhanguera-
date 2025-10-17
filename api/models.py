from django.db import models

class Tutor(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True, help_text="Formato: 000.000.000-00")
    email = models.EmailField(max_length=255, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_completo
