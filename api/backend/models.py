from django.db import models
from django.db.models.fields import AutoField, CharField, DateTimeField, TextField

class Relatorio(models.Model):
    
    id = AutoField(primary_key=True)
    data_busca = DateTimeField(auto_now_add=True)
    dados = TextField()
    repositorio = CharField(max_length=255, default='NI')
    organizacao = CharField(max_length=255, default='NI')

    class Meta:
        app_label = 'api'