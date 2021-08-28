from django.contrib import admin
from .models import Mensagem, Atendimento, Cliente

# Register your models here.

admin.site.register(Mensagem)
admin.site.register(Atendimento)
admin.site.register(Cliente)