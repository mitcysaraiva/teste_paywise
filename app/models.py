from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)

class Doador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    cidade = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)

class Campanha(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=300)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    cidade = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)