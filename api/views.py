#from django.shortcuts import render

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from api.serializers import TaskSerializer
from api.models import Task

from .tasks import add

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
        resultado = add.delay(10, 10)
        print(resultado)
        # Retorna la respuesta original del método create
        return response
