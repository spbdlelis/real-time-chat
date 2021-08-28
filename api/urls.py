from rest_framework.routers import SimpleRouter

from .views import (
    ClienteViewSet,
    AtendimentoViewSet,
    MensagemViewSet
)

router = SimpleRouter()
router.register('clientes', ClienteViewSet)
router.register('atendimentos', AtendimentoViewSet)
router.register('mensagens', MensagemViewSet)
