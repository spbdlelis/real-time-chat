from celery import shared_task
from .models import Cliente, Atendimento, Mensagem

@shared_task
def create_automatic_response(self, request, *args, **kwargs):
    atd = request.data['atendimento']
    atendimento = Atendimento.objects.get(id=atd)
    Mensagem.objects.create(
        atendimento=atendimento,
        texto='Bem vindo, Essa mensagem é automática',
        tipo='e',
        status='v'
    )

