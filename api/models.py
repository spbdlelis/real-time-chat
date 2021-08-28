from django.db import models


class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField(max_length=255, blank=False, null=False)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} ({self.telefone})'

class Atendimento(Base):
    cliente = models.ForeignKey(Cliente, related_name='clientes',  on_delete=models.CASCADE)
    organizacao = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=1, choices=[
        ('s', 'Atendido'),
        ('n', 'Não Atendido'),
    ])

    def __str__(self):
        return f'{self.cliente} da(o) {self.organizacao}: {self.status}'


class Mensagem(Base):
    atendimento = models.ForeignKey(Atendimento, related_name='atendimentos', on_delete=models.DO_NOTHING)
    texto = models.TextField(blank=True, null=True)
    arquivo = models.FileField(null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=[
        ('r', 'Recebido'),
        ('e', 'Enviado')
    ], blank=False, null=False)
    status = models.CharField(max_length=1, choices=[
        ('t', 'Entregue'),
        ('v', 'Enviado'),
        ('l', 'Lido'),
    ], blank=False, null=False)

    def __str__(self):
        return f'{self.criado_em.strftime("%d/%m/%Y,  %H:%M:%S")} : {self.texto} // Tipo: {self.tipo}'





