#from django.shortcuts import render

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .serializers import TaskSerializer
from .models import Task

#from .tasks import add


from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_mail():
    # Procesar los datos que desea enviar por correo electrónico
    user = {
        'name' : 'Jorge'
    }
    destination = "xxxxx@gmail.com"

    # Renderizar un template HTML con los datos procesados
    context = {'user': user}
    message = render_to_string('mails/account/locked.html', context)

    # Crear un objeto EmailMessage y enviar el correo electrónico
    mail = EmailMessage(
        '{} Tu cuenta ha sido bloqueda.'.format(user.get('name')),
        message,
        'xxxxx@gmail.com',
        [destination],
        reply_to=['xxxxxx@gmail.com']
    )
    mail.content_subtype = "html"  # Para enviar el correo con formato HTML
    mail.send()


@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de tareas.'),
    retrieve=extend_schema(description='Permite obtener una tarea.'),
    create=extend_schema(description='Permite crear una tarea.'),
    update=extend_schema(description='Permite actualizar una tarea.'),
    destroy=extend_schema(description='Permite eliminar una tarea.'),
)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        # Llamada al método create original
        response = super().create(request, *args, **kwargs)

        # Agrega código adicional aquí para extender la funcionalidad del método post
        #resultado = add.delay(10, 10)
        #print(resultado)
        # Retorna la respuesta original del método create

        # TEST DE ENVIO DE CORREOS
        send_mail()

        return response





