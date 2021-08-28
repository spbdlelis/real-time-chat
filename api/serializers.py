from rest_framework import serializers
from .models import Mensagem, Atendimento, Cliente

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = (
            'id',
            'texto',
            'arquivo',
            'tipo',
            'status',
            'criado_em',
            'modificado_em',
            'atendimento',
        )


class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = (
            'id',
            'cliente',
            'organizacao',
            'status',
        )


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'nome',
            'telefone',
        )
