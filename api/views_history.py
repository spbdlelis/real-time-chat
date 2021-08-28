from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente, Atendimento, Mensagem
from .serializers import ClienteSerializer, AtendimentoSerializer, MensagemSerializer

class ClienteAPIView(APIView):
    """
    API de Clientes da aplicação
    """

    def get(self, request):
        clientes = Cliente.objecs.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


class AtendimentoAPIView(APIView):
    """
    API de Atendimentos da aplicação
    """

    def get(self, request):
        atendimentos = Atendimento.objecs.all()
        serializer = ClienteSerializer(atendimentos, many=True)
        return Response(serializer.data)


class MensagemAPIView(APIView):
    """
    API de Mensagens da aplicação
    """

    def get(self, request):
        mensagens = Mensagem.objecs.all()
        serializer = ClienteSerializer(mensagens, many=True)
        return Response(serializer.data)
