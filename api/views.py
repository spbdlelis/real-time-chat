from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Cliente, Atendimento, Mensagem
from .serializers import ClienteSerializer, AtendimentoSerializer, MensagemSerializer
from rest_framework.decorators import action
from rest_framework import mixins
from .tasks import create_automatic_response

class ClienteViewSet(
    viewsets.ModelViewSet
):
    """
    DOCSTRING
    API de Clientes da aplicação
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=True, methods=['GET'])
    def atendimentos(self, request, pk):
        cliente = self.get_object()
        serializer = AtendimentoSerializer(Atendimento.objects.filter(cliente=cliente), many=True)
        return Response(serializer.data)


class AtendimentoViewSet(
    viewsets.ModelViewSet
):
    """
    DOCSTRING
    API de Atendimentos da aplicação
    """
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer


class MensagemViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    #mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """
    DOCSTRING
    API de Mensagens da aplicação
    """
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

    def create(self, request, *args, **kwargs):
        create_automatic_response(self, request, args, kwargs)
        return super(MensagemViewSet, self).create(request, *args, **kwargs)
