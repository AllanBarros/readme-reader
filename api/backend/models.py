from django.db import models
from django.db.models.fields import AutoField, DateTimeField, TextField

class Relatorio(models.Model):
    id = AutoField(primary_key=True)
    data_busca = DateTimeField(auto_now_add=True)
    dados = TextField()